from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
# from .forms import CommentForm
from django.utils import timezone



def details(request):
    heejae = 'Matilda'
    return render(request,'listing/details.html',{'a':heejae})



def details2(request):
    heejae = 'Matilda'
    return render(request,'listing/details2.html',{'a':heejae})