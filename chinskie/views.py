from django.shortcuts import render
from django.http import HttpResponse
from chinskie import dbhandler
from django.template import loader
import re

def sanitize(_str): return re.sub('[^a-zA-Z0-9ążźĘęćłńóśĄŻŹĆŁŃÓŚ \n\.]', '', _str)

def index(request):
    return HttpResponse(str(dbhandler.get_all('class', '3f')))

def columns(request):
    return HttpResponse(str(dbhandler.get_column_names()))

def class_get(request, klasa):
    japierdole, empty = dbhandler.get_essential('class', klasa)
    context = {
        'essential': japierdole,
        'cotojest': sanitize(klasa),
        'empty': empty,
        'czego': 'takiej klasy.'
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def teacher_get(request, nauczyciel):
    japierdole, empty = dbhandler.get_essential('teacher', nauczyciel)
    context = {
        'essential': japierdole,
        'cotojest': sanitize(nauczyciel),
        'empty': empty,
        'czego': 'takiego nauczyciela.'
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def classroom_get(request, classroom):
    japierdole, empty = dbhandler.get_essential('classroom', classroom)
    context = {
        'essential': japierdole,
        'cotojest': sanitize(classroom),
        'empty': empty,
        'czego': 'takiej sali lekcyjnej.'
    }
    template = loader.get_template('zupki/tabelka.html')
    return HttpResponse(template.render(context, request))

def teacher_list(request):
    nauczyciele = dbhandler.get_teachers()
    context = {
        'essential': nauczyciele,
        'cotojest': 'Nauczyciele',
        'czego': 'Lista nauczycieli.'
    }
    template = loader.get_template('zupki/lista.html')
    return HttpResponse(template.render(context, request))

def class_list(request):
    nauczyciele = dbhandler.get_classes()
    context = {
        'essential': nauczyciele,
        'cotojest': 'Klasy',
        'czego': 'Lista klas.'
    }
    template = loader.get_template('zupki/lista.html')
    return HttpResponse(template.render(context, request))
def classroom_list(request):
    nauczyciele = dbhandler.get_classrooms()
    context = {
        'essential': nauczyciele,
        'cotojest': 'Sale lekcyjne',
        'czego': 'Lista sal lekcyjnych.'
    }
    template = loader.get_template('zupki/lista.html')
    return HttpResponse(template.render(context, request))