from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "users/register.html",
                          context={"form":form})

    form = CustomUserCreationForm
    return render(request = request,
                  template_name = "users/register.html",
                  context={"form":form})