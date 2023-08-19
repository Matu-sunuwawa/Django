from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Saving,Credit
from django.contrib.auth.models import User
from django.views import View

# Create your views here.

class HomePage(LoginRequiredMixin, View):
    def get(self,request):
        return render(request, 'users/select.html')
    def post(self,request):
        return render(request, 'users/select.html')

class Register(View):
    def get(self,request):
         # return HttpResponse("Hello World")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} your account is created successfully!!')
            sav = Saving(name = username.lower(), amt = 0)
            cred = Credit(name = username.lower(), amt = 0)
            sav.save()
            cred.save()
            return redirect('select')
        # else:
        #     form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self,request):
        # return HttpResponse("Hello World")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} your account is created successfully!!')
            sav = Saving(name = username.lower(), amt = 0)
            cred = Credit(name = username.lower(), amt = 0)
            sav.save()
            cred.save()
            return redirect('select')
        # else:
        #     form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

class Profile(LoginRequiredMixin,View):
    def profile(request):
        return render(request, 'users/profile.html')

class Select(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/select.html')
    def post(self,request):
        return render(request, 'users/select.html')

class Savingacc(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/savingacc.html')
    def post(self,request):
        # view = request.POST.get('View')
        # obj = Saving.objects,all()
        # datad = Saving.objects.filter(name= request.user) 
        # named = request.GET.get('name')
        # namew = request.GET.get('name')
        # deposit = request.GET.get('deposit')
        # withdraw = request.GET.get('withdraw')
        # Saving.objects.filter(name = request.user).update(amt=ndept)
        return render(request, 'users/user/savingacc.html')

class Savingaccadmin(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/admin/savingaccadmin.html')
    def post(self,request):
        return render(request, 'users/admin/savingaccadmin.html')

class Chooseuser(LoginRequiredMixin,View):
    # def __init__(self,request,*args,**kwargs):
    #     self.user = request.POST['login']
    def get(self,request):
        global user
        user = request.POST['login']
        data = Saving.objects.filter(name= user.lower())
        for a in data:
            if a.name == user.lower():            
                return redirect('selectadmin')
        return render(request, 'users/profile.html', {})
    def post(self,request):
        global user
        user = request.POST['login']
        data = Saving.objects.filter(name= user.lower())
        for a in data:
            if a.name == user.lower():            
                return redirect('selectadmin')
        return render(request, 'users/profile.html', {})

class Selectadmin(LoginRequiredMixin,View):
    def get(self,request):
        data = Saving.objects.filter(name= user.lower())
        for a in data:
            nuser = a.name
        return render(request, 'users/admin/selectadmin.html', {'nuser': nuser})
    def post(self,request):
        data = Saving.objects.filter(name= user.lower())
        for a in data:
            nuser = a.name
        return render(request, 'users/admin/selectadmin.html', {'nuser': nuser})

class Viewsav(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.is_superuser:
            data = Saving.objects.filter(name= user.lower()) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/admin/savingaccadmin.html', {'camt': namt})
        else:
            data = Saving.objects.filter(name= request.user) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/user/savingacc.html', {'camt': namt})
    def post(self,request):
        if request.user.is_superuser:
            data = Saving.objects.filter(name= user.lower()) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/admin/savingaccadmin.html', {'camt': namt})
        else:
            data = Saving.objects.filter(name= request.user) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/user/savingacc.html', {'camt': namt})
    
class Transferone(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/transfer.html')
    def post(self,request):
        return render(request, 'users/user/transfer.html')
    
class Transfertwo(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/transfer.html')
    def post(self,request):
        try:
            global name,amt
            name = request.POST['name']
            # name = name.title()
            amt = int(request.POST['amount'])
            data = Saving.objects.all()
            ndata = Saving.objects.filter(name= request.user)
            for b in ndata:
                if b.name == name.lower():
                    messages.info(request, 'Action Denying!!')
                    return render(request, 'users/user/savingacc.html')
            for a in data:
                if a.name == name.lower():
                    if amt < 0 :
                        messages.info(request, 'There is no such inputs!!')
                        return render(request, 'users/user/savingacc.html')
                    elif amt > int(a.amt):
                        messages.info(request, 'There is no enough balance!!')
                        return render(request, 'users/user/savingacc.html')
                    else:
                        return render(request, 'users/user/validation.html', {'name':name.title(),'amt':amt})
            messages.info(request, 'There is no such User!')
            return render(request, 'users/user/savingacc.html')
        except:
            return render(request, 'users/select.html')
class Transferthree(Transfertwo,LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        data = Saving.objects.all()
        udata = Saving.objects.filter(name= request.user)
        fdata = Saving.objects.filter(name= name)
        for a in udata:
            namt = int(a.amt) - amt
            new_dept = Saving.objects.filter(name = request.user).update(amt=namt)
            messages.info(request, 'your request Successfully DONE!!')
        for b in fdata:
            namt = int(b.amt) + amt
            new_dept = Saving.objects.filter(name = name).update(amt=namt)
        return render(request, 'users/user/savingacc.html')
            

class Depositsav(LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        if request.user.is_superuser:
            # user = request.POST['login']
            data = Saving.objects.filter(name= user)
            deposit = int(request.POST['deposit'])
            for a in data:
                if deposit < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('savingacc')
                else:
                    ndept = int(a.amt) + deposit
            new_dept = Saving.objects.filter(name = user).update(amt=ndept)
            return redirect('select')
        else:
            datad = Saving.objects.filter(name= request.user) 
            # named = request.POST.get('name')
            # deposit = request.POST.get('deposit')
            deposit = int(request.POST['deposit'])
            for a in datad:
                if deposit < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('savingacc')
                else:
                    ndept = int(a.amt) + deposit
            new_dept = Saving.objects.filter(name = request.user).update(amt=ndept)
            return redirect('select')
        # return render(request, 'users/user/savingacc.html', {})

class Withdrawsav(LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        if request.user.is_superuser:
            # user = request.POST['login']
            data = Saving.objects.filter(name= user) 
            withdraw = int(request.POST['withdraw'])
            for a in data:
                if withdraw < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('savingacc')
                elif withdraw > int(a.amt):
                    messages.info(request, 'There is no enough money!!')
                    return redirect('savingacc')
                else:
                    nwith = int(a.amt) - withdraw
            new_dept = Saving.objects.filter(name = user).update(amt=nwith)
            return redirect('select')
        else:
            datad = Saving.objects.filter(name= request.user) 
            # named = request.POST.get('name')
            # deposit = request.POST.get('deposit')
            withdraw = int(request.POST['withdraw'])
            for a in datad:
                if withdraw < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('savingacc')
                elif withdraw > int(a.amt):
                    messages.info(request, 'There is no enough money!!')
                    return redirect('savingacc')
                else:
                    nwith = int(a.amt) - withdraw
            new_dept = Saving.objects.filter(name = request.user).update(amt=nwith)
            return redirect('select')
        # return render(request, 'users/user/savingacc.html', {})

# class Creditacc(LoginRequiredMixin,View):
#     def creditacc(request):
#         return render(request, 'users/user/creditacc.html')
class Creditacc(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/creditacc.html')
    def post(self,request):
        return render(request, 'users/user/creditacc.html')
    
class Creditaccadmin(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/admin/creditaccadmin.html')
    def post(self,request):
        return render(request, 'users/admin/creditaccadmin.html')

class Viewcred(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.is_superuser:
            data = Credit.objects.filter(name= user.lower()) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/admin/creditaccadmin.html', {'camt': namt})
        else:
            data = Credit.objects.filter(name= request.user) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/user/creditacc.html', {'camt': namt})
    def post(self,request):
        if request.user.is_superuser:
            data = Credit.objects.filter(name= user.lower()) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/admin/creditaccadmin.html', {'camt': namt})
        else:
            data = Credit.objects.filter(name= request.user) 
            # name = request.GET.get('name')
            for a in data:
                namt = int(a.amt)
            return render(request, 'users/user/creditacc.html', {'camt': namt})
        
class Transferonecred(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/transfercred.html')
    def post(self,request):
        return render(request, 'users/user/transfercred.html')
    
class Transfertwocred(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'users/user/transfercred.html')
    def post(self,request):
        try:
            global name,amt
            name = request.POST['name']
            # name = name.title()
            amt = int(request.POST['amount'])
            data = Credit.objects.all()
            ndata = Credit.objects.filter(name= request.user)
            for b in ndata:
                if b.name == name.lower():
                    messages.info(request, 'Action Denying!!')
                    return render(request, 'users/user/creditacc.html')
            for a in data:
                if a.name == name.lower():
                    if amt < 0 :
                        messages.info(request, 'There is no such inputs!!')
                        return render(request, 'users/user/creditacc.html')
                    else:
                        return render(request, 'users/user/validationcred.html', {'name':name.title(),'amt':amt})
            messages.info(request, 'There is no such User!')
            return render(request, 'users/user/creditacc.html')
        except:
            return render(request, 'users/select.html')
        
class Transferthreecred(Transfertwocred,LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        data = Credit.objects.all()
        udata = Credit.objects.filter(name= request.user)
        fdata = Saving.objects.filter(name= name)
        for a in udata:
            namt = int(a.amt) + amt
            new_dept = Credit.objects.filter(name = request.user).update(amt=namt)
            messages.info(request, 'your request Successfully DONE!!')
        for b in fdata:
            namt = int(b.amt) + amt
            new_dept = Saving.objects.filter(name = name).update(amt=namt)
        return render(request, 'users/user/creditacc.html')
    
class Depositcred(LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        if request.user.is_superuser:
            # user = request.POST['login']
            data = Credit.objects.filter(name= user)
            deposit = int(request.POST['deposit'])
            for a in data:
                if deposit < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('creditacc')
                elif deposit > int(a.amt):
                    messages.info(request, 'It is not saving account keep free from Credit!!')
                    return redirect('creditacc')
                else:
                    ndept = int(a.amt) - deposit
            new_dept = Credit.objects.filter(name = user).update(amt=ndept)
            return redirect('select')
        else:
            datad = Credit.objects.filter(name= request.user) 
            # named = request.POST.get('name')
            # deposit = request.POST.get('deposit')
            deposit = int(request.POST['deposit'])
            for a in datad:
                if deposit < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('creditacc')
                elif deposit > int(a.amt):
                    messages.info(request, 'It is not saving account keep free from Credit!!')
                    return redirect('creditacc')
                else:
                    ndept = int(a.amt) - deposit
            new_dept = Credit.objects.filter(name = request.user).update(amt=ndept)
            return redirect('select')

class Withdrawcred(LoginRequiredMixin,View):
    def get(self,request):
        pass
    def post(self,request):
        if request.user.is_superuser:
            # user = request.POST['login']
            data = Credit.objects.filter(name= user) 
            withdraw = int(request.POST['withdraw'])
            for a in data:
                if withdraw < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('creditacc')
                else:
                    nwith = int(a.amt) + withdraw
            new_dept = Credit.objects.filter(name = user).update(amt=nwith)
            return redirect('select')
        else:
            datad = Credit.objects.filter(name= request.user) 
            # named = request.POST.get('name')
            # deposit = request.POST.get('deposit')
            withdraw = int(request.POST['withdraw'])
            for a in datad:
                if withdraw < 0:
                    messages.info(request, 'There is no such inputs!!')
                    return redirect('Creditacc')
                else:
                    nwith = int(a.amt) + withdraw
            new_dept = Credit.objects.filter(name = request.user).update(amt=nwith)
            return redirect('select')