from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Python. I am Django...")

def hello(request):
    return HttpResponse("Hello World")

def post(request):
    return HttpResponse("Welcome")

def comment(request):
    return HttpResponse("Welcome to Comments")