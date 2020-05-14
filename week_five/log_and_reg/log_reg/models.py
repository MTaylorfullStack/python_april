from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors['first_name'] = "Your first name must be at least 2 characters."
        if len(postData['lname']) < 2:
            errors['last_name'] = "Your last name must be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "You email must be a valid email."
        if len(postData['pw']) < 8:
            errors['password'] = "Your password must be at least 8 characters."
        if postData['pw'] != postData['confpw']:
            errors['conf_password'] = "You password and confirm password must match."
        return errors
        
        


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()