from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime
# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render_to_response('base.html', locals())
def current_datetime(request):
    #now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    #return render_to_response('current_datetime.html', {'current_date': now})
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
