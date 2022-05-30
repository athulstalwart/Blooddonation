from django.urls import path

from credapp import views

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('donate',views.donate,name='donate')
]