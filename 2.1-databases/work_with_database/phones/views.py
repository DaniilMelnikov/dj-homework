from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')

def sort_object(object, sort):
    if sort == 'min_price':
        sorting = sorted([f'{el.price}' for el in object])
    elif sort == 'max_price':
        sorting = sorted([f'{el.price}' for el in object], reverse=True)
    else:
        sorting = sorted([f'{el.name}' for el in object])
    phones = []
    for el in sorting:
        count = -1
        while len(phones) != len(object):
            count += 1
            if object[count].name == el:
                phones.append(object[count])
                break
            if str(object[count].price) == el:
                phones.append(object[count])
                break
    return phones

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    phones = sort_object(phones, sort)
    context = {
        'phones': phones,
    }
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
