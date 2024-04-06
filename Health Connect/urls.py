from django.urls import path
from . import views

urlpatterns = [
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
]
