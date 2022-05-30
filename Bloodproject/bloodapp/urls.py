from django.urls import path

from bloodapp import views

urlpatterns=[
    path('',views.index,name='index'),
]