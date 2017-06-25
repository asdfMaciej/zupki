from django.shortcuts import render
from django.http import HttpResponse
from chinskie import dbhandler

def index(request):
    return HttpResponse(str(dbhandler.get_all('class', '3f')))

def columns(request):
    return HttpResponse(str(dbhandler.get_column_names()))

def class_get(request, klasa):
    return HttpResponse(str(dbhandler.get_essential('class', klasa)))

def teacher_get(request, nauczyciel):
    return HttpResponse(str(dbhandler.get_essential('teacher', nauczyciel)))

def teacher_list(request):
    return HttpResponse(str(dbhandler.get_teachers()))