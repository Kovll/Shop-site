from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductsCategory, Products, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
# контроллеры, вьюхи = функции

def index(request):
    context = {
        'title': 'StoreShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'Каталог - Store', 'categories': ProductsCategory.objects.all()}
    if category_id:
        products = Products.objects.filter(category_id=category_id)
    else:
        products = Products.objects.all()
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)


# Добавления товара в корзину
@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



