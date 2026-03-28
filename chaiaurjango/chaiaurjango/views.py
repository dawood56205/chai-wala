from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("hello, world, this is home page")
  return render(request, 'index.html')

def about(request):
  return HttpResponse("hello, world, this is about page")

def contact(request):
  return HttpResponse("hello, world, this is contact page")