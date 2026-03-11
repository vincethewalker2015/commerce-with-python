from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if category_slug:
    category = Category.objects.get(slug=category_slug)
    products = products.filter(category=category)
  return render(request, 'products/product/list.html', {'category': category, 'categories': categories, 'products': products})
