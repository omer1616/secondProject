from django.urls import path

from . import views


urlpatterns = [
    path('', views.list_company),
    path('list-company/', views.list_company, name="list_company"),
    path('add-company/', views.add_company,  name="add_company"),
    path('list-person/', views.list_person, name="list_person"),
    path('add-person/', views.add_person,  name="add_person"),
]

