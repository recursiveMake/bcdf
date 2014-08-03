__author__ = 'adonis'


from django import forms


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
    recaptcha_challenge_field = forms.CharField(widget=forms.HiddenInput())
    recaptcha_response_field = forms.CharField(widget=forms.HiddenInput())


class SearchForm(forms.Form):
    pass


class PaypalForm(forms.Form):
    cmd = forms.CharField(widget=forms.HiddenInput(attrs={'value': '_s-xclick'}))
    hosted_button_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'VYYB7YQFFMS4J'}))
    submit = forms.ImageField()
