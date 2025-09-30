from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),   
    path("list/", views.employee_list, name="employee_list"),
    path("add/", views.employee_create, name="employee_create"),
    path("edit/<int:pk>/", views.employee_update, name="employee_update"),
    path("delete/<int:pk>/", views.employee_delete, name="employee_delete"),
]
