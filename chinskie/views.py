from django.shortcuts import render
from django.http import HttpResponse
from chinskie import dbhandler
from django.template import loader

def index(request):
    return HttpResponse(str(dbhandler.get_all('class', '3f')))

def columns(request):
    return HttpResponse(str(dbhandler.get_column_names()))

def class_get(request, klasa):
    return HttpResponse(str(dbhandler.get_essential('class', klasa)))

def teacher_get(request, nauczyciel):
    japierdole = dbhandler.get_essential('teacher', nauczyciel)
    context = {
        'essential': japierdole,
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def teacher_list(request):
    return HttpResponse(str(dbhandler.get_teachers()))