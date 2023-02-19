from django.urls import path

from . import views


urlpatterns = [
    path('', views.list_company),
    path('list-company/', views.list_company, name="list_company"),
    path('list-company/<int:id>', views.company_detail, name="company_detail"),
    path('list-company/update/<int:id>', views.company_update, name="company_update"),
    path('add-company/', views.add_company,  name="add_company"),
    path('list-person/', views.list_person, name="list_person"),
    path('add-person/', views.add_person,  name="add_person"),
    path('list-company/<int:id>/delete', views.delete_company,  name="delete_company"),
]

