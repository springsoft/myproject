# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("网站建设中，请关注!")

def api(request):
    return JsonResponse({'status':100, 'message':'event name already exists'})
