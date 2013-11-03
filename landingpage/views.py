from django.shortcuts import render


def hello(request):
    base_data = {
        'title': 'hello Dawid',
        'content': 'Hello world & Dawid'
    }
    return render(request, 'base.html', base_data)
