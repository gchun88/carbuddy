from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
# from .forms import CommentForm
from django.utils import timezone

from listing.models import CarInstance

def details(request):
    heejae = 'Matilda'
    return render(request,'listing/details.html',{'a':heejae})



def details2(request):
    heejae = 'Matilda'
    return render(request,'listing/details2.html',{'a':heejae})


class CarInstanceListView(generic.ListView):
	model = CarInstance
	template_name = 'listing/car_list.html'
# paginate_by = 10
# def get_queryset(self):
# 	return Car.objects.values_list('brand', flat=True).distinct()
# def testlink1(request):
#     html = '<html><body><a href="carmodels/">carmodel List</a></body></html>'
#     return HttpResponse(html)