from django.shortcuts import render, get_object_or_404
from django.http import *
from forms import FlightForm, ProjectForm
from models import Flight, Project
from django.http import Http404
from django.template import Context
from gps.analysers import Charts, Point_model, Maps

def home(request):
    flight = Flight.objects.all()
    projects = Project.objects.all()
    homedata = {"homedata":{"flight": flight, "projects": projects}}
    return render(request, 'home.html', homedata)

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return HttpResponseRedirect('/')
        else:
            raise Http404
        
    else:
        form = FlightForm()
        return render(request, 'add_flight.html', {"form": form})


def delete_flight(request, id):
    queryset = Flight.objects.all()
    instance = get_object_or_404(queryset, id=id)
    instance.delete()
    return HttpResponseRedirect('/')

def mapsviews(request, id):
    maps = Maps(id)
    data = maps.context()
    return render(request, 'maps.html', Context(data))

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponseRedirect('/')
        else:
            raise Http404
        
    else:
        form = ProjectForm()
        return render(request, 'add_project.html', {"form": form})

def delete_project(request, id):
    queryset = Project.objects.all()
    instance = get_object_or_404(queryset, id=id)
    instance.delete()
    return HttpResponseRedirect('/')

def analyse(request, id):
    charts = Charts(id)
    data = charts.curve_chart()
    return render(request, 'analyse.html', {"data": data})

def point(request, id):
    point = Point_model(id)
    data = point.view()
    return render(request, 'point.html', {"data":data})

def about(request):
    return render(request, 'about.html')
