from django.db import models
from unittest.util import _MAX_LENGTH
from django.template.defaultfilters import default
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text



@python_2_unicode_compatible
class Driver(models.Model):
    driver_name = models.CharField(max_length=200)
    driver_sex = models.CharField(max_length=4)
    driver_age = models.IntegerField(default=18)
    
    img = models.ImageField(upload_to="photos")
    
    def __str__(self):
        return self.driver_name
    
@python_2_unicode_compatible
class Comment(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=20)
    comment_num = models.IntegerField(default=0)
    
    def __str__(self):
        return self.comment_text
    

class User(models.Model):
    username = models.CharField(max_length=20)
    userpwd =  models.CharField(max_length=20)
    
    
