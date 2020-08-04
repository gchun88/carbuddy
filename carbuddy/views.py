from django.http import HttpResponse
from django.shortcuts import render
import datetime

from django.views import generic


def index(request):
	#View function for home page of site
	return render(request, 'headfoot/index.html',{})

def testlink2(request):
    html = '<html><body><a href="details/">carmodel Details</a></body></html>'
    return HttpResponse(html)

