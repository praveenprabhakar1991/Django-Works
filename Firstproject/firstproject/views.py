# This View File is Created by Prabhakar

from django.http import HttpResponse

def index(request):
     return HttpResponse("<h1> Welcome to Django World </h1>")

def github(request):
     return HttpResponse("<a href = 'https://github.com/praveenprabhakar1991'> <h2> Github page </h2> </a>")

def youtube(request):
     return HttpResponse("<a href = 'https://www.youtube.com/watch?v=mB34HoNog6U'> <h2> Youtube Page </h2> </a>")

def facebook(request):
     return HttpResponse("<a href = 'https://www.facebook.com/prabhakarbonez'> <h2> Facebook page </h2> </a>")

def instagram(request):
     return HttpResponse("<a href = 'https://www.instagram.com/praveen_prabhakar_/'> <h2> Instagram page </h2> </a> <a href = '/'> Home Page </a>")