from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,  JsonResponse
from .models import *
from .forms import CompanyForm

# Create your views here.


def list_company(request):
    company = Company.objects.all()
    context = {
        'companies': company
    }

    return render(request, 'directory/list_company.html', context=context)


def add_company(request):
    form = CompanyForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "test":" fdsf"
    }
    return render(request, 'directory/add_company.html', context=context)


def delete_company(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return JsonResponse({"status": "True"})

def list_person(request):
    company = Company.objects.all()
    context = {
        'company': company
    }

    return render(request, 'directory/list_person.html' )


def add_person(request):


    return render(request, 'directory/add_person.html',)
