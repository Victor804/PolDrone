from django.shortcuts import render, get_object_or_404
from django.http import *
from forms import ProcessingNodeForm
from models import ProcessingNode
from django.http import Http404
import gpxpy
import gpxpy.gpx

def home(request):
    processingnode = ProcessingNode.objects.all()
    return render(request, 'home/index.html', {'processingnodes': processingnode})

def add_flight(request):
    if request.method == 'POST':
        form = ProcessingNodeForm(request.POST)
        print form.errors
        if form.is_valid():  
            print form
            form.save()
            return HttpResponseRedirect('/')
        else:
            raise Http404
        
    else:
        form = ProcessingNodeForm()
        return render(request, 'form/index.html', {"form": form})


def delete_flight(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    instance.delete()
    return HttpResponseRedirect('/')

def mapsviews(request, id):
    queryset = ProcessingNode.objects.all()
    instance = get_object_or_404(queryset, id=id)
    path_gpx = instance.gpx
    gpx_file = open(unicode(path_gpx), 'r')
    
    gpx = gpxpy.parse(gpx_file)
    flightcoodinates = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                flightcoodinates.append("{"+"lat:{0}, lng:{1}".format(point.latitude, point.longitude)+"},")
    center = flightcoodinates[0]
    flightcoodinates = "".join(flightcoodinates)
    return render(request, 'maps/index.html', {"flightcoodinates": flightcoodinates}, {"center": center})
    