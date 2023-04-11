from django.shortcuts import render
from .models import ProductCategory, Product

def home(request):
    return render(request, 'products/index.html')

def products(request):
    context = {
        'title': 'Catalog',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)