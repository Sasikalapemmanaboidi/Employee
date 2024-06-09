from django.contrib import admin
from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee_createlabel/', views.employee_createlabel, name='employee_createlabel'),
    path('employee_editlabel/<str:username>/', views.employee_editlabel, name='employee_editlabel'),
    path('employee_content/', views.employee_content, name='employee_content'),
    path('employee_delete/<str:username>/', views.employee_delete, name='employee_delete'),
]  

