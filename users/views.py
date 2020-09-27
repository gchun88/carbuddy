from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username,password=raw_password)
                login(request, user)
                return redirect("index")
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])

                return render(request = request,
                              template_name = "account/register.html",
                              context={"form":form})

        form = CustomUserCreationForm
        return render(request = request,
                      template_name = "account/register.html",
                      context={"form":form})

