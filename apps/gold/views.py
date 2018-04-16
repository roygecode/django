from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.

# request.session = {} //a dictionary
# request.session = {
#     'gold=0'
# }

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['log'] = []
    print request.session['log']
    return render(request,'gold/index.html')

def process(request, loc):
    if request.method !="POST":  
        return redirect('/')

    if loc =='farm':
        gold = random.randrange(10,21)
        log_str = ("gain","Earned {} gold from the {} ({})".format(gold,loc,datetime.datetime.now()))    #interpolating technique in Django
                                                                                                         #will turn to string for you
    if loc == 'cave':
        gold = random.randrange(5,11)
        log_str = ("gain","Earned {} gold from the {} ({})".format(gold,loc,datetime.datetime.now()))
    
    if loc == 'house':
        gold = random.randrange(2,6)
        log_str = ("gain","Earned {} gold from the {} ({})".format(gold,loc,datetime.datetime.now()))
    
    if loc == 'casino':
        gold = random.randrange(-50,51)
        if gold < 0:
            log_str = ("loss","Lost {} gold from the {} ({})".format(abs(gold),loc,datetime.datetime.now()))
        else:
            log_str = ("gain","Earned {} gold from the {} ({})".format(gold,loc,datetime.datetime.now()))

    
    
    request.session['gold'] += gold
    currlog = request.session['log']        
    # request.session['log'].insert(0,log_str)   //cause django does not like accesing session and print to index
    currlog.insert(0,log_str)
    request.session['log'] = currlog
    print request.session['log']
    return redirect('/')

def reset(request):
    # del request.session['gold'] // will work for one
    
    
    request.session.clear()  # this clears everything
    return redirect('/')
