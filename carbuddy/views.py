from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
	#View function for home page of site
	return render(request, 'index.html') 


# def testlink1(request):
#     html = '<html><body><a href="carmodels/">carmodel List</a></body></html>'
#     return HttpResponse(html)



def testlink2(request):
    html = '<html><body><a href="details/">carmodel Details</a></body></html>'
    return HttpResponse(html)

