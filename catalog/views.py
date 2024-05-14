from django.shortcuts import render, redirect

from catalog.models import Product, Contact

APP_TITLE = 'SF Store'
context = {'app_title': APP_TITLE}

paginate_by = 3


def index(request):
    return render(request, 'catalog/index.html')


def product_list(request, page=1):

    products = Product.objects.all()
    pages = len(products) // paginate_by + 1

    return render(request, 'catalog/product_list.html',
                  context=context | {'products': products[paginate_by * (page - 1): paginate_by * page],
                                     'pages': range(1, pages)})


def product_details(request, pk):
    product = Product.objects.filter(pk=pk).first()

    print(product.image)
    return render(request, 'catalog/details.html',
                  context=context | {'product': product})


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
