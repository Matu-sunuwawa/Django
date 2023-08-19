from django.db import models

# Create your models here.
class Saving(models.Model):
    name = models.CharField(max_length=100)
    amt = models.IntegerField()
    # des = models.TextField()
    def __str__(self):
        return self.name
    
class Credit(models.Model):
    name = models.CharField(max_length=100)
    amt = models.IntegerField()
    # des = models.TextField()
    def __str__(self):
        return self.name
    
"""
I Learnt sth-------------

class City(models.Model):
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    name_regex = RegexValidator(regex=r'^[a-zA-Z]+$',
                                message="Name should only consist of characters")
    name = NameField(validators=[name_regex], max_length=100)
    postalcode = models.IntegerField(unique=True)
"""