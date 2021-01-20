from django.shortcuts import render,redirect,HttpResponse
from .models import product


# Create your views here.
def main(request):
	products = product.objects.all()

	no_of_products = len(products)
	params = {'range' : range(no_of_products),'products' : products}
	return render(request,'index.html',params)


def login(request):
	return render(request,'login.html')


def productview(request ,myid):
	product_req = product.objects.filter(id=myid)


	return render(request, 'product-single.html', 
		{'product':product_req[0]})


def about(request):
	return HttpResponse("works")

def contact(request):
	return HttpResponse("works")

def cart(request):
	return render(request,'cart.html')
