# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import *
from ..LoginReg.models import *

def dashboard(request):
    try:
        logged_User = User.objects.get(id = request.session['user_id'])
        context = {
                'loggeduser': logged_User,
                'my_wishlist': Wishlist.objects.filter(Q(added_by = logged_User) | Q(wished_by = logged_User)),
                'all_wishlist': Wishlist.objects.all(),
                'others_wishlist': Wishlist.objects.all().exclude(added_by = logged_User),
        }
        return render(request, 'WishlistApp/dashboard.html', context)
    except:
        context = {
                'all_user': User.objects.all(),
                'all_wishlist': Wishlist.objects.all(),
        }
        return render(request, 'WishlistApp/dashboard.html', context)

def create_item(request):
    try:
        logged_User = User.objects.get(id = request.session['user_id'])
        context = {
                'loggeduser': logged_User,
        }
        return render(request, 'WishlistApp/create_wish.html', context)
    except:
        return redirect('/main')

def create_item_process(request):
    if request.method == 'POST':
        result = Wishlist.objects.Wish(request.POST)
        if 'err_messages' in result:
            for e in result['err_messages']:
                messages.error(request, e)
                return redirect('/wish_items/create')
        else:
            return redirect('/dashboard')
    pass

def destroy(request, item_id):
    item = Wishlist.objects.get(id=int(item_id))
    item.delete()
    return redirect('/dashboard')

def item_remove(request, item_id):
    item = Wishlist.objects.get(id=int(item_id))
    try:
        logged_User = User.objects.get(id = request.session['user_id'])
        logged_User(wished_by = item.id).delete()
        return redirect('/dashboard')
    except:
        return redirect('/dashboard')

def item_page(request, item_id):
    item = Wishlist.objects.get(id=int(item_id))
    owner = User.objects.filter(item_added = item.id)
    context = {
                'item':item,
                'owner': owner,
                'allwished': User.objects.filter(item_wished = item.id).exclude(item_added = item.id),
        }
    return render(request, 'WishlistApp/product_page.html', context)

def item_wishfor(request, item_id):
    logged_User = User.objects.get(id = request.session['user_id'])
    item = Wishlist.objects.get(id=int(item_id))
    logged_User.item_wished.add(item)
    return redirect('/dashboard')
