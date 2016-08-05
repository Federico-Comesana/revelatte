from django.shortcuts import render, redirect
from .forms import RegistrationForm


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, "registration/registration_form.html",
                  {"form": form})
