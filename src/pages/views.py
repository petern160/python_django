from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    print (args, kwargs)
    # return HttpResponse("<h1>hello world<h1>") 
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
      return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
      
    my_context = {
          "my_text": "this is about us",
          "my_number": 123,
          "my_list": [123, 123, 321, 32134, "abc"],
          "my_html": "<h1>hello world</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>social<h1>") #