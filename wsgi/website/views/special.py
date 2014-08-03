__author__ = 'adonis'


from website.models import SpecialArticle, BannerCampaign, HomePageCampaign
from website.forms import ContactForm
from website.views.util import update_context, article_parse
from utils.recaptcha_keys import RecaptchaKey
from utils import recaptcha, ip
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
import random


def home_index(request):
    banner_campaigns = BannerCampaign.objects.all().filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    home_page_campaigns = HomePageCampaign.objects.all().filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    n = home_page_campaigns.count()
    if n > 4:
        indices = sorted(random.sample(range(0, n), 4))
        home_page_campaigns = [home_page_campaigns[idx] for idx in indices]
    context = {
        'banner_campaigns': banner_campaigns,
        'home_page_campaigns': home_page_campaigns
    }
    update_context(request, context)
    return render(request, 'website/home/index.html', context)


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            keys = RecaptchaKey(request)
            captcha_resp = recaptcha.submit(
                form.cleaned_data['recaptcha_challenge_field'],
                form.cleaned_data['recaptcha_response_field'],
                keys.private_key,
                ip.get_client_ip(request)
            )
            if captcha_resp.is_valid:
                send_mail(
                    subject='Contact Page message',
                    message=form.cleaned_data['comments'],
                    from_email=form.cleaned_data['email'],
                    recipient_list=['bcdfoundation@gmail.com', 'yoshimitsu12@gmail.com']
                )
                messages.success(request, "Thank you for your email.")
                return redirect('home:index')
            else:
                messages.error(request, "Invalid reCAPTCHA response.")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = ContactForm()
    keys = RecaptchaKey(request)
    context = {
        'form': form,
        'recaptcha': recaptcha.displayhtml(public_key=keys.public_key)
    }
    update_context(request, context)
    return render(request, 'website/special/contact.html', context)


def special_article(request, article_id):
    response = get_object_or_404(SpecialArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    if response.template == SpecialArticle.STANDARD:
        return render(request, 'website/special/article.html', context)
    if response.template == SpecialArticle.MULTI_IMAGE:
        return render(request, 'website/special/multi-image.html', context)

