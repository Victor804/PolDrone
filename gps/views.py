from django.shortcuts import render, get_object_or_404
from django.http import *
from forms import ProcessingNodeForm, ProjectForm
from models import ProcessingNode, Project
from django.http import Http404
from django.conf import settings
from django.template import Context
from gps.analysers import extract_xml_to_maps

def home(request):
    processingnodes = ProcessingNode.objects.all()
    projects = Project.objects.all()
    homedata = {"homedata":{"processingnodes": processingnodes, "projects": projects}}
    return render(request, 'home.html', homedata)

def add_flight(request):
    if request.method == 'POST':
        form = ProcessingNodeForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return HttpResponseRedirect('/')
        else:
            raise Http404
        
    else:
        form = ProcessingNodeForm()
        return render(request, 'add_flight.html', {"form": form})


def delete_flight(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    instance.delete()
    return HttpResponseRedirect('/')

def mapsviews(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    path_xml_file = instance.xml_file
    xml_file = open(settings.MEDIA_ROOT + str(path_xml_file), 'r')
    gpsdata = extract_xml_to_maps(xml_file)
    return render(request, 'maps.html', Context(gpsdata))

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
    return render(request, 'analyse.html')