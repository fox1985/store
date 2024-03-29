from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import  Paginator

def index(request):
    context = {
        'title': 'Stor'
    }
    return  render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):
    # фильтрация по категориям
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    par_page = 3
    paginator = Paginator(products, par_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Stor - Каталог',
        'categorys': ProductCategory.objects.all(),
        'products' :products_paginator
    }

    return  render(request, 'products/products.html', context)

@login_required()
def basket_add(request, product_id):
    "Добавляем в карзину"
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def basket_delete(request, id):
    "Удалить из карзины"
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))