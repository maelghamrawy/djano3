from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def login(request):
    if request.method == "POST":
        dataForm = LoginForm(request.POST)
        if dataForm.is_Valid():
            dataForm.save()
    return render(request, 'loginForm.html',{'loginForm': LoginForm})
