from django.shortcuts import render
from django.http import HttpResponse
from shop_app.models import Product , Client


def index(request):
	products = Product.objects.all()
	return render(request, 'index.html', context={ 'products' : products})


def product(request , product_id ):
	product = Product.objects.get(id=product_id)
	return render(request, 'product.html', context={ 'product' : product})


def clients(request):
	clients = Client.objects.all()[:30]
	return render(request, 'clients.html', context={ 'clients' : clients })


def client(request, client_id):
	client = Client.objects.get(id=client_id)
	return render(request, 'client.html', context={ 'client' : client })
