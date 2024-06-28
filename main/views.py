from django.shortcuts import render, get_object_or_404
from .models import Shirt, Shorts, Sneakers


def index(request):
    shirt_top = Shirt.objects.filter(top=True)
    shorts_top = Shorts.objects.filter(top=True)
    sneakers_top = Sneakers.objects.filter(top=True)
    
    shirt_discounted = Shirt.objects.exclude(discount=None).exclude(discount=0)
    shorts_discounted = Shorts.objects.exclude(discount=None).exclude(discount=0)
    sneakers_discounted = Sneakers.objects.exclude(discount=None).exclude(discount=0)
    
    context = {
        'shirt_top': shirt_top,
        'shorts_top': shorts_top,
        'sneakers_top': sneakers_top,
        'shirt_discounted': shirt_discounted,
        'shorts_discounted': shorts_discounted,
        'sneakers_discounted': sneakers_discounted,
    }
    return render(request, 'index/index.html', context=context)

def buy_shirt(request, pk):
    shirt = get_object_or_404(Shirt, pk=pk)
    
    if shirt.discount:
        shirt.discounted_price = round(shirt.price * (1 - shirt.discount / 100), 2)
    else:
        shirt.discounted_price = shirt.price
    
    context = {
        'product': shirt
    }
    return render(request, 'product/buy.html', context)

def buy_shorts(request, pk):
    shorts = get_object_or_404(Shorts, pk=pk)
    
    if shorts.discount:
        shorts.discounted_price = round(shorts.price * (1 - shorts.discount / 100), 2)
    else:
        shorts.discounted_price = shorts.price
    
    context = {
        'product': shorts
    }
    return render(request, 'product/buy.html', context)

def buy_sneakers(request, pk):
    sneakers = get_object_or_404(Sneakers, pk=pk)
    
    if sneakers.discount:
        sneakers.discounted_price = round(sneakers.price * (1 - sneakers.discount / 100), 2)
    else:
        sneakers.discounted_price = sneakers.price
    
    context = {
        'product': sneakers
    }
    return render(request, 'product/buy.html', context)

def shorts(request):
    data = Shorts.objects.all()

    unique_sizes = data.values_list('size', flat=True).distinct()
    unique_colors = data.values_list('color', flat=True).distinct()
    unique_companies = data.values_list('company', flat=True).distinct()

    size_filter = request.GET.getlist('size')
    color_filter = request.GET.getlist('color')
    company_filter = request.GET.getlist('company')

    if size_filter:
        data = data.filter(size__in=size_filter)
    if color_filter:
        data = data.filter(color__in=color_filter)
    if company_filter:
        data = data.filter(company__in=company_filter)
        
    for item in data:
        if item.discount:
            item.discounted_price = round(item.price * (1 - item.discount / 100), 2)
        else:
            item.discounted_price = item.price
            
    context = {
        'data': data,
        'unique_sizes': unique_sizes,
        'unique_colors': unique_colors,
        'unique_companies': unique_companies,
        'selected_sizes': size_filter,
        'selected_colors': color_filter,
        'selected_companies': company_filter
    }
    return render(request, 'product/shorts.html', context=context)    

def shirt(request):
    data = Shirt.objects.all()

    unique_sizes = data.values_list('size', flat=True).distinct()
    unique_colors = data.values_list('color', flat=True).distinct()
    unique_companies = data.values_list('company', flat=True).distinct()

    size_filter = request.GET.getlist('size')
    color_filter = request.GET.getlist('color')
    company_filter = request.GET.getlist('company')

    if size_filter:
        data = data.filter(size__in=size_filter)
    if color_filter:
        data = data.filter(color__in=color_filter)
    if company_filter:
        data = data.filter(company__in=company_filter)

    for item in data:
        if item.discount:
            item.discounted_price = round(item.price * (1 - item.discount / 100), 2)
        else:
            item.discounted_price = item.price    

    context = {
        'data': data,
        'unique_sizes': unique_sizes,
        'unique_colors': unique_colors,
        'unique_companies': unique_companies,
        'selected_sizes': size_filter,
        'selected_colors': color_filter,
        'selected_companies': company_filter
    }
    return render(request, 'product/shirt.html', context=context)

def sneakers(request):
    data = Sneakers.objects.all()

    unique_sizes = data.values_list('size', flat=True).distinct()
    unique_colors = data.values_list('color', flat=True).distinct()
    unique_companies = data.values_list('company', flat=True).distinct()

    size_filter = request.GET.getlist('size')
    color_filter = request.GET.getlist('color')
    company_filter = request.GET.getlist('company')

    if size_filter:
        data = data.filter(size__in=size_filter)
    if color_filter:
        data = data.filter(color__in=color_filter)
    if company_filter:
        data = data.filter(company__in=company_filter)
        
    for item in data:
        if item.discount:
            item.discounted_price = round(item.price * (1 - item.discount / 100), 2)
        else:
            item.discounted_price = item.price        

    context = {
        'data': data,
        'unique_sizes': unique_sizes,
        'unique_colors': unique_colors,
        'unique_companies': unique_companies,
        'selected_sizes': size_filter,
        'selected_colors': color_filter,
        'selected_companies': company_filter
    }
    return render(request, 'product/sneakers.html', context=context)