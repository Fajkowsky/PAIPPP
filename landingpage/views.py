from django.shortcuts import render
from landingpage.forms import RegisterForm


def hello(request):
    base_data = {
        'title': 'hello Dawid',
        'content': 'Hello world & Dawid'
    }
    return render(request, 'index.html', base_data)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':  # If the form has been submitted...
        form = RegisterForm(request.POST)  # A form bound to the POST data
    if form.is_valid():  # All validation rules pass
        # Process the data in form.cleaned_data
        # ...
        return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = RegisterForm()  # An unbound form

    return render(request, 'register.html', {
                  'form': form,
                  })
