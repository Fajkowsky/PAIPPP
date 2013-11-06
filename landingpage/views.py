from django.shortcuts import render


def hello(request):
    base_data = {
        'title': 'hello Dawid',
        'content': 'Hello world & Dawid'
    }
    return render(request, 'index.html', base_data)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
