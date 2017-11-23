# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        match_email = re.match(EMAIL_REGEX, str(postData['email']))
        errors = []
        if match_email == None:
            errors.append('Invalid Email Format.')
        if len(postData['password']) < 8:
            errors.append('Password must be 8 characters or more. ')
        if len(postData['name']) < 2:
            errors.append('Name must be more than 2 characters or more.')
        if len(postData['alias']) < 3:
            errors.append('Alias must be more than 2 characters or more.')
        if(postData['password'] != postData['confirm_password']):
            errors.append("Password and password confirmation don't match.")

        try:
            #this line is checking to see if the email is already in the database
            User.objects.get(email = postData['email'])
            errors.append("A user with this email already exists. Please login.")
        except:
            pass

        if errors:
            return {'err_messages': errors}
        else:
            #These two lines create the hashed password and use
            hash_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name = postData['name'], email = postData['email'], password = hash_pw)

            # In order to log this user in we need to return the user object that we just created back to the views
            return {'new_user': user}

    def login(self, postData):
        try:
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                return {'logged_user': user}
            else:
                return {'err_messages': ['Email/Password invalid. Please try again.']}
        # If a user with that email does not exist in the database, send back an error message
        except:
            return {'err_messages': ['Email does not exists. Please register']}

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
