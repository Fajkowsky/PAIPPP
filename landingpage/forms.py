from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    nick = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    city = forms.CharField(max_length=60)
    country = forms.CharField(max_length=50)
    terms = forms.BooleanField()