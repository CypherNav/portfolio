from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"main/index.html")
def projects(request):
    return render(request,'main/projects.html')
def language(request):
   return render(request,'main/language.html')



