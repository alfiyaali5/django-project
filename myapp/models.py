from django.db import models

# Create your models here.

 
class Member(models.Model):
 def __str__(self) -> str:
    return self.firstname
   
 firstname=  models.CharField(max_length=225)
 lastname=  models.CharField(max_length=225)
 rollno= models.IntegerField(null=True)
 image= models.ImageField(default='default.jpeg',upload_to='member_photo/')
