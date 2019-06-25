from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>hello world<h1>") #string of html code

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact<h1>") #