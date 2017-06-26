from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^klasa/(?P<klasa>[a-zA-Z0-9ążźćłńóśęĘĄŻŹĆŁŃÓŚ\/ \n\.]+)/$', views.class_get, name='class_get'),
    url(r'^nauczyciel/(?P<nauczyciel>[a-zA-Z0-9ążźćęĘłńóśĄŻŹĆŁŃÓŚ\- \n\.]+)/$', views.teacher_get, name='teacher_get'),
    url(r'^sala/(?P<classroom>[a-zA-Z0-9ążźćłęĘńóśĄŻŹĆŁŃÓŚ \n\.]+)/$', views.classroom_get, name='classroom_get'),
    url(r'^nauczyciel/$', views.teacher_list, name='teacher_list'),
    url(r'^klasa/$', views.class_list, name='class_list'),
    url(r'^sala/$', views.classroom_list, name='classroom_list')
]