from django.shortcuts import render, redirect
from django import template
from django.http.response import HttpResponse
import uuid
from .models import Url

# Create your views here.

def url(request):
    return render(request, 'shortener/url.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
