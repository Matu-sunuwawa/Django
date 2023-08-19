from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'HomePage'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('select/', views.Select.as_view(), name='select'),
    path('selectadmin/', views.Selectadmin.as_view(), name='selectadmin'),
    path('savingacc/', views.Savingacc.as_view(), name='savingacc'),
    path('savingaccadmin/', views.Savingaccadmin.as_view(), name='savingaccadmin'),
    path('chooseuser/', views.Chooseuser.as_view(), name='chooseuser'),
    path('viewsav/', views.Viewsav.as_view(), name='viewsav'),
    path('trans/', views.Transferone.as_view(), name='trans'),
    path('transfer/', views.Transfertwo.as_view(), name='transfer'),
    path('transfering/', views.Transferthree.as_view(), name='transfering'),
    path('depositsav/', views.Depositsav.as_view(), name='depositsav'),
    path('withdrawsav/', views.Withdrawsav.as_view(), name='withdrawsav'),
    path('creditacc/', views.Creditacc.as_view(), name='creditacc'),
    path('creditaccadmin/', views.Creditaccadmin.as_view(), name='creditaccadmin'),
    path('viewcred/', views.Viewcred.as_view(), name='viewcred'),
    path('transcred/', views.Transferonecred.as_view(), name='transcred'),
     path('transfercred/', views.Transfertwocred.as_view(), name='transfercred'),
     path('transferingcred/', views.Transferthreecred.as_view(), name='transferingcred'),
     path('depositcred/', views.Depositcred.as_view(), name='depositcred'),
     path('withdrawcred/', views.Withdrawcred.as_view(), name='withdrawcred'),
    path('login/',auth_view.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
]
