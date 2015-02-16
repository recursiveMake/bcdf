__author__ = 'adonis'


from website.models import CalendarCampaign
from website.views.util import update_context, paginate
from django.shortcuts import render


def calendar_index(request):
    calendar_list = CalendarCampaign.objects.all().order_by('expiry')
    calendar_list = paginate(request, calendar_list)
    context = {
        'calendar_list': calendar_list,
    }
    update_context(request, context)
    return render(request, 'website/calendar/index.html', context)