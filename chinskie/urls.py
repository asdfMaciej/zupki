from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^klasa/(?P<klasa>[a-zA-Z0-9ążźćłńóśĄŻŹĆŁŃÓŚ \n\.]+)/$', views.class_get, name='class_get'),
    url(r'^nauczyciel/(?P<nauczyciel>[a-zA-Z0-9ążźćłńóśĄŻŹĆŁŃÓŚ \n\.]+)/$', views.teacher_get, name='teacher_get'),
    url(r'^nauczyciel/$', views.teacher_list, name='teacher_list'),
    url(r'^klasa/$', views.class_list, name='class_list'),
    url(r'^columns$', views.columns, name='columns')
]