from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators

from .models import UnicodeMobileNumberValidator, EmailChecker
from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': "شماره موبال خود را وارد کنید","value":"09124569873"}
        ),
        label='شماره موبایل',
        required=True,
        max_length=11,
        validators=[
            UnicodeMobileNumberValidator(),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': "پسورد را وارد کنید","value":"superUser123987456"}),
        label='پسورد',
        required=True,
        min_length=10,
    )

    def clean_password(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        is_user = User.objects.filter(phone=phone).exists()
        if not is_user:
            raise forms.ValidationError('شماره موبایل یا پسورد اشتباه است')
        return password


class RegisterForm(forms.Form):
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': "شماره موبال خود را وارد کنید"}
        ),
        label='شماره موبایل',
        required=True,
        max_length=11,
        validators=[
            UnicodeMobileNumberValidator(),
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': "ایمیل را وارد کنید"}
        ),
        label='ایمیل',
        required=True,
        max_length=50,
        validators=[
            validators.EmailValidator(),
            EmailChecker(),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': "پسورد را وارد کنید"}),
        label='پسورد',
        required=True,
        min_length=10,
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': "تکرار پسورد"}),
        label='پسورد 2',
        required=True,
        min_length=10,
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_user = User.objects.filter(phone=phone).exists()
        if is_user:
            raise forms.ValidationError(
                'این شماره موبایل قبلا استفاده شده است')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')

        is_email = User.objects.filter(email=email).exists()
        if is_email:
            raise forms.ValidationError('ایمیل قبلا استفاده شده است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('پسورد ها مثل هم نیستن')


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(
        widget=forms.NumberInput(),
        required=True,
        max_length=11,
        validators=[
            UnicodeMobileNumberValidator(),
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),
        required=True,
        max_length=50,
        validators=[
            validators.EmailValidator(),
            EmailChecker(),
        ]
    )

    class Meta:
        model = User
        fields = ('email', 'phone')


class CustomUserChangeForm(UserChangeForm):
    phone = forms.CharField(
        widget=forms.NumberInput(),
        required=True,
        max_length=11,
        validators=[
            UnicodeMobileNumberValidator(),
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),
        required=True,
        max_length=50,
        validators=[
            validators.EmailValidator(),
            EmailChecker(),
        ]
    )

    class Meta:
        model = User
        fields = ('email', 'phone')
