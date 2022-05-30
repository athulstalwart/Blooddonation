from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('disp/',views.display,name='display'),

    path('ajax/load-cities/', views.load_center, name='center'),  # AJAX
]