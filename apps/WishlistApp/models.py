# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LoginReg.models import User

class WishlistValid(models.Manager):
    def Wish(self, postData):
        errors = []
        if len(postData['product']) == 0:
            errors.append('No empty entries allowed!!')
        elif len(postData['product']) < 3:
            errors.append('Item name should be more than 3 characters')

        if errors:
            return {'err_messages': errors}
        else:
            #user_id is not a good way of doing this, but just for the exam! :)
            item = Wishlist.objects.create(item = postData['product'], added_by = User.objects.get(id = postData['user_id']), wished_by = User.objects.get(id = postData['user_id']))
            return {'new_item':item}

class Wishlist(models.Model):
    item = models.CharField(max_length = 255)
    added_by = models.ForeignKey(User, related_name = 'item_added')
    wished_by = models.ForeignKey(User, related_name= 'item_wished')
    date_added = models.DateTimeField(auto_now_add = True)
    objects = WishlistValid()
