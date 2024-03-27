from django.shortcuts import render, get_object_or_404

from .models import Category, ProductProxy


def products_view(requests):
    products = ProductProxy.objects.all()
    return render(requests, 'shop/products.html', {'products': products})


def product_detail_view(requests, slug):
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(requests, 'shop/product_detail.html', {'product': product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related('category').filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'shop/category_list.html', context)
