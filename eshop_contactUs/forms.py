from django import forms
from django.core import validators

from eshop_account.models import EmailChecker


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "نام و نام خانوادگی خود را وارد کنید", 'class':'form-control'}
        ),
        label='نام و نام خانوادگی',
        required=True,
        max_length=100,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': "ایمیل را وارد کنید", 'class': 'form-control'}
        ),
        label='ایمیل',
        required=True,
        max_length=100,
        validators=[
            validators.EmailValidator(),
            EmailChecker(),
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "موضوع خود را وارد کنید",
                   'class': 'form-control'}
        ),
        label='موضوع',
        required=True,
        max_length=200,
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': "متن خود را وارد کنید",
                   'class': 'form-control h-75 d-inline-block', 'rows': 8,'style':'height:200px' }
        ),
        label='متن',
        required=True,
        max_length=250,
    )

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name) == 0 or len(full_name) >100:
            raise forms.ValidationError('نام و نام خانوادگی نامعتبر است')
        return full_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '' or len(email) > 100:
            raise forms.ValidationError('ایمیل نامعتبر است')
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if subject == '' or len(subject) > 200:
            raise forms.ValidationError('موضوع نامعتبر است')
        return subject

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text == '' or len(text) > 250:
            raise forms.ValidationError('متن نامعتبر است')
        return text
    

