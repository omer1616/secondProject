from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import CompanyForm , PersonForm


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
        "test": " fdsf"
    }
    return render(request, 'directory/add_company.html', context=context)


def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    print(company)
    context = {
        "company": company
    }
    return render(request, "directory/company_detail.html", context=context)


def company_update(request, id):
    company = get_object_or_404(Company, id=id)
    form = CompanyForm(request.POST, request.FILES or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect('list_company')

    context = {
        'form': form
    }

    return render(request, 'directory/company_update.html', context=context)

@csrf_exempt
def delete_company(request, id):

    company = get_object_or_404(Company, id=id)
    company.delete()
    return HttpResponse(reverse('list_company'))


def list_person(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }

    return render(request, 'directory/list_person.html')


def add_person(request):
    form = PersonForm(request.POST,  request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
         "form": form
     }

    return render(request, 'directory/add_person.html', context=context)
