# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index(request):
    return render(request, "LoginReg/index.html")

def process(request):
    if request.method == 'POST':
        logic_id = int(request.POST['logic_id'])
        if logic_id == 1: #Register Form
            result = User.objects.register(request.POST)
            if 'err_messages' in result:
                for e in result['err_messages']:
                    messages.error(request, e)
            else:
                request.session['user_id'] = result['new_user'].id
                print('New user registered')
                return redirect('/dashboard')

        if logic_id == 2: #Login Form
            result = User.objects.login(request.POST)
            if 'err_messages' in result:
                for e in result['err_messages']:
                    messages.error(request, e)
            else:
                request.session['user_id'] = result['logged_user'].id
                return redirect('/dashboard')

    return redirect('/main')

def logout(request):
    del request.session['user_id']
    return redirect('/main')
