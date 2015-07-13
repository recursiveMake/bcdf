__author__ = 'adonis'


from website.models import SpecialArticle, BannerCampaign, HomePageCampaign
from website.forms import ContactForm
from website.views.util import render, article_parse
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from datetime import datetime
import random


def home_index(request):
    banner_campaigns = BannerCampaign.objects.published(request.production).filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    home_page_campaigns = HomePageCampaign.objects.published(request.production).filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    n = home_page_campaigns.count()
    if n > 8:
        indices = sorted(random.sample(range(0, n), 8))
        home_page_campaigns = [home_page_campaigns[idx] for idx in indices]
    context = {
        'banner_campaigns': banner_campaigns,
        'home_page_campaigns': home_page_campaigns
    }
    return render(request, 'website/home/index.html', context)


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject='Contact Page message',
                message=form.cleaned_data['comments'],
                from_email=form.cleaned_data['email'],
                recipient_list=['bcdfoundation@gmail.com', 'adelia@bovellcancerdiabetesfoundation.org']
            )
            messages.success(request, "Thank you for your email.")
            return redirect('home:index')
        else:
            messages.error(request, "Invalid form data. Did you complete the captcha?")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'website/special/contact.html', context)


def donate_form(request):
    response = get_object_or_404(SpecialArticle, slug='donate')
    (request, context) = article_parse(request, response)
    return render(request, 'website/special/donate.html', context)


def special_article(request, article_id):
    response = get_object_or_404(SpecialArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    if response.template == SpecialArticle.STANDARD:
        return render(request, 'website/special/article.html', context)
    if response.template == SpecialArticle.MULTI_IMAGE:
        return render(request, 'website/special/multi-image.html', context)

