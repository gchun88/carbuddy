from django.http import HttpResponse
from django.shortcuts import render
import datetime
from listing.models import Car
from django.views import generic


def index(request):
	#View function for home page of site
	return render(request, 'index.html') 


class CarListView(generic.ListView):
	model = Car
	# paginate_by = 10

# def testlink1(request):
#     html = '<html><body><a href="carmodels/">carmodel List</a></body></html>'
#     return HttpResponse(html)



def testlink2(request):
    html = '<html><body><a href="details/">carmodel Details</a></body></html>'
    return HttpResponse(html)

