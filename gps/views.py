from django.shortcuts import render, get_object_or_404
from django.http import *
from forms import ProcessingNodeForm
from models import ProcessingNode
from django.http import Http404
from django.conf import settings
from django.template import Context
from gps.analysers import maps

def home(request):
    processingnode = ProcessingNode.objects.all()
    return render(request, 'home.html', {'processingnodes': processingnode})

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
        return render(request, 'form.html', {"form": form})


def delete_flight(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    instance.delete()
    return HttpResponseRedirect('/')

def mapsviews(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    path_gpx = instance.gpx
    gpx_file = open(settings.MEDIA_ROOT + str(path_gpx), 'r')
    gpsdata = maps(gpx_file)
    return render(request, 'maps.html', Context(gpsdata))

def analyse(request, id):
    return render(request, 'analyse.html')