__author__ = 'adonis'


from website.models import EducationalArticle
from website.views.util import update_context, article_parse
from django.shortcuts import render, get_object_or_404


def education_index(request):
    article_list = EducationalArticle.objects.all().order_by('-pub_date')[:10]
    context = {
        'article_list': article_list,
        'url_namespace': 'education:article',
        'read_on_message': 'Read on for more details...'
    }
    update_context(request, context)
    return render(request, 'website/education/index.html', context)


def education_index_by_year(request, year):
    article_list = EducationalArticle.objects.all().order_by('-pub_date')
    article_list = article_list.filter(pub_date__year=year)
    context = {
        'article_list': article_list,
        'url_namespace': 'education:article',
        'read_on_message': 'Read on for more details...'
    }
    update_context(request, context)
    return render(request, 'website/education/index.html', context)


def education_article(request, article_id):
    response = get_object_or_404(EducationalArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    if response.specialimage_set.all():
        # has multi-images
        return render(request, 'website/education/multi-image.html', context)
    return render(request, 'website/education/article.html', context)


