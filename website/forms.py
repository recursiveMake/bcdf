__author__ = 'adonis'


from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-large',
                'placeholder': 'Your Name',
                'required': ""
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-large',
                'placeholder': 'A valid email address',
                'required': "",
                'type': 'email'
            }
        )
    )
    comments = forms.CharField(
        label='Comments',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '6',
                'required': ""
            }
        )
    )
    captcha = ReCaptchaField(public_key=None, private_key=None)


class SearchForm(forms.Form):
    pass

