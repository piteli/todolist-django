from django.db import models


class Parent(models.Model):
    #to store the name of the user
    tdlistParent = models.CharField(max_length=100)
    #to store the email of the user
#    email = models.CharField(max_length=100)
    #to store the password of the user
#    password = models.CharField(max_length=100)

class Child(models.Model):
    tdlistChild = models.CharField(max_length=100)
    complete = models.NullBooleanField()
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, blank=True, null=True)


#this returns the name of the user when the object of user is printed
