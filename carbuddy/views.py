from django.http import HttpResponse
from django.shortcuts import render
import datetime
from listing.models import CarInstance
from django.views import generic


def index(request):
	#View function for home page of site
	return render(request, 'index.html') 


class CarInstanceListView(generic.ListView):
	model = CarInstance
	template_name = 'listing/car_list.html'
	# paginate_by = 10
	
	# def get_queryset(self):
	# 	return Car.objects.values_list('brand', flat=True).distinct()

# def testlink1(request):
#     html = '<html><body><a href="carmodels/">carmodel List</a></body></html>'
#     return HttpResponse(html)



def testlink2(request):
    html = '<html><body><a href="details/">carmodel Details</a></body></html>'
    return HttpResponse(html)

