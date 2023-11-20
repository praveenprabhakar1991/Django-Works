from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
def index(request):
     # return HttpResponse(' <h1> Welcome To Shop App </h1>')
     # Products = Product.objects.all()
     # print(Products)
     # n = len(Products)

     allProds = []
     CategoryProds = Product.objects.values('Category', 'id')
     Categories = {item['Category'] for item in CategoryProds}
     for Cat in Categories:
          Prod = Product.objects.filter(Category = Cat)
          n = len (Prod)
          nslides = n//4 + ceil((n/4))-(n//4)
          allProds.append([Prod, range(1,nslides), nslides])
     # parameters = {'no_of_slides' : nslides, 'range' : range(1,nslides), 'Product' : products}
     # allProds = [[Products, range(1, nslides), nslides],
     #             [Products, range(1, nslides), nslides]]
     parameters = {'allProds' : allProds}
     return render(request, 'shop/index.html', parameters)

def about(request):
     return render(request, 'shop/about.html')

def contact(request):
     return render(request, 'shop/contact.html')

def tracker(request):
     return render(request, 'shop/tracker.html')

def search(request):
     return render(request, 'shop/search.html')

def productview(request, myid):
     #Fetching the Product using Id
     product = Product.objects.filter(id=myid)
     return render(request, 'shop/productview.html', {'product': product[0]})

def checkout(request):
     return render(request, 'shop/checkout.html')