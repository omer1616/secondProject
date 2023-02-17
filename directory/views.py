from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):

    company = Company.objects.all()
    context = {
        'company': company
    }

    return render(request, 'base.html', context=context)