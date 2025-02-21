from django.shortcuts import render, HttpResponse
from .models import MyModel
from .forms import MyModelForm  
# Create your views here.

def home(request):
    return render(request, "home.html")

def list(request):
    person = MyModel.objects.all()
    return render(request, "home.html",{ 'person': person })