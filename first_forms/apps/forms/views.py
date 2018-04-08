from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from forms import RegistrationForm
# then create an index method:
def index(request):
    form = RegistrationForm() # We will build this class out in just a minute
    context = {
        'myregistrationform': form # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'formtest/index.html', context)

def reigster(request):
    if request.method == "POST":
        bound_form = RegistrationForm(request.POST)
        print bound_form.is_valid()
        print bound_form.error
        return redirect ('/')
