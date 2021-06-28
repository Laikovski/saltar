from django.shortcuts import render, redirect
import datetime
from .forms import UpperForm
from .models import GetUserInfo, Services
from bot.send_message import send_message
from django.http import JsonResponse

def open_main_page(request):
    """Rendering main page, work with form requests"""
    x = datetime.datetime.now()
    services = Services.objects.all()
    form = UpperForm(request.POST or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['phone'] = form.cleaned_data.get('phone')

            send_message(data['name'], data['phone'])
            return JsonResponse(data)


    context = {'form': form, 'year': x.year, 'services': services}
    return render(request, 'main/index.html', context)









