from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse, request


# Create your views here.
def index(request):
    return render(request, "index.html")
def adminlogin(request):
    return render(request, "adminlogin.html")
