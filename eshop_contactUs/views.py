from django.shortcuts import render

from .forms import ContactUsForm
from .models import ContactUs
from eshop_settings.models import Settings

# Create your views here.


def contact_us_view(request):
    seting = Settings.objects.first()
    contact_us_form = ContactUsForm(request.POST or None)

    if contact_us_form.is_valid():
        full_name = contact_us_form.cleaned_data.get('full_name')
        email = contact_us_form.cleaned_data.get('email')
        subject = contact_us_form.cleaned_data.get('subject')
        text = contact_us_form.cleaned_data.get('text')
        ContactUs.objects.create(
            full_name=full_name, email=email, subject=subject, text=text)

        contact_us_form = ContactUsForm()

    context = {
        'contact_us_forms': contact_us_form,
        'aboutUs': seting
    }
    return render(request, 'contactUs\contact_us.html', context)
