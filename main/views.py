from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Homepage view"""
    return HttpResponse("<h1>Welcome to Your Python App Download Site!</h1><p>Your Django project is working!</p>")
