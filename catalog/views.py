from django.shortcuts import render, redirect

from catalog.models import Product, Contact

APP_TITLE = 'SF Store'
context = {'app_title': APP_TITLE}


def product_list(request):
    products = Product.objects.all()

    return render(request, 'catalog/product_list.html',
                  context=context | {'products': products})


def product_details(request, pk):
    return render(request, 'catalog/details.html', context=context)


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
