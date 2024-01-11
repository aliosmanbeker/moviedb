from django.shortcuts import render
from .models import category,Movie


def home(request):
    data = {
        "kategoriler":category.objects.all,
        "filmler":Movie.objects.filter(anasayfa=True)
    }
    return render(request,"index.html",data)
def movies(request):
    data = {
        "kategoriler":category.objects.all,
        "filmler":Movie.objects.all
    }
    return render(request,"movies.html",data)
def moviedetails(request,id):
    data = {
        "movie":Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)
