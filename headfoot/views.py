from django.shortcuts import render

# Create your views here.
def test(request):
    heejae = 'Matilda'
    return render(request,'headfoot/test.html',{'a':heejae})
