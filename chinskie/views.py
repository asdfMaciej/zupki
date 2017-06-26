from django.shortcuts import render
from django.http import HttpResponse
from chinskie import dbhandler
from django.template import loader
import re

def sanitize(_str): return re.sub('[^a-zA-Z0-9ążźćłńóśĄŻŹĆŁŃÓŚ \n\.]', '', _str)

def index(request):
    return HttpResponse(str(dbhandler.get_all('class', '3f')))

def columns(request):
    return HttpResponse(str(dbhandler.get_column_names()))

def class_get(request, klasa):
    japierdole = dbhandler.get_essential('class', klasa)
    context = {
        'essential': japierdole,
        'cotojest': sanitize(klasa)
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def teacher_get(request, nauczyciel):
    japierdole = dbhandler.get_essential('teacher', nauczyciel)
    context = {
        'essential': japierdole,
        'cotojest': sanitize(nauczyciel)
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def teacher_list(request):
    return HttpResponse(str(dbhandler.get_teachers()))
def class_list(request):
    return HttpResponse(str(dbhandler.get_classes()))