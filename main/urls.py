from django.urls import path
from django.urls import re_path
from . import views

urlpatterns=[
    path('add/',views.std, name='added'),
    path('',views.index, name='index'),
    path('view/',views.view, name='view'),
    path('delete/<int:id>',views.dele, name='delete'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('saveedit/<int:id>',views.saveedit, name='saveedit'),
    re_path(r'^postData$', views.pdata, name='pdata'),
] 