from django.shortcuts import render, redirect

APP_TITLE = 'SF Store'
context = {'app_title': APP_TITLE}


def index(request):
    return render(request, 'catalog/index.html',
                  context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return redirect('catalog:home')

    else:
        return render(request, 'catalog/contacts.html',
                      context=context)
