from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app1.models import *

from django.http import HttpResponse
# class CBV_ListForm(ListView):
#     model=School
#     template_name='CBV_ListForm.html'
#     context_object_name='SFO'
#     # ordering=['name']


def CBV_List_view(request,na):
    return HttpResponse(f'hello this is Mr/Mrs   {na}')
