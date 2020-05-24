from django.shortcuts import render
from .models import Form
# Create your views here.

def home(request):
    return render (request, 'index.html')


def create(request):
 if request.method=="POST":
    form = Form()
    form.name = request.POST["name"]
    form.number = request.POST["number"]
    form.time = request.POST["time"]
    form.choice = request.POST["choice"]
    form.save()
    return render(request, 'index.html')