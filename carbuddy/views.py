from django.http import HttpResponse
import datetime

def testlink1(request):
    html = '<html><body><a href="carmodels/">carmodel List</a></body></html>'
    return HttpResponse(html)



def testlink2(request):
    html = '<html><body><a href="details/">carmodel Details</a></body></html>'
    return HttpResponse(html)

