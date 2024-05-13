from django.shortcuts import render, redirect

from catalog.models import Product, Contact

APP_TITLE = 'SF Store'
context = {'app_title': APP_TITLE}


def index(request):
    products = Product.objects.all()

    return render(request, 'catalog/base.html',
                  context=context | {'products': products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return redirect('catalog:home')

    else:
        contacts = Contact.objects.all().values()[0]
        return render(request, 'catalog/contacts.html',
                      context=context | contacts)
