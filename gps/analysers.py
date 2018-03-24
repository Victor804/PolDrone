from lxml import etree
from gps.models import Project, Flight, Point
from django.conf import settings

class Charts(object):
    def __init__(self, id):
        self.id = id
        self.point = Point_viewer(id)
    def curve_chart(self):
        self.point.add()
        data = [['time', 'CO2', 'NH3', 'NOx']]
        points = Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))
        for point in points:
            data.append([(point.time).encode('utf-8'), point.c02, point.nh3, point.nox])
        return data
    
class Point_viewer(object):
    def __init__(self, id):
        self.id = id

    def add(self):        
        path_xml_file = Flight.objects.all().get(id=self.id).xml_file
        xml_file = (settings.MEDIA_ROOT + str(path_xml_file))
        tree = etree.parse(xml_file)
        if str(Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))) == "<QuerySet []>" or str(Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))) == "[]":
            for xml in tree.xpath("/trkseg/trkpt"):
                Point(flight=Flight.objects.all().get(id=self.id), lat=float(xml.get("lat")), lon=float(xml.get("lon")), time=xml.get("hour"), c02=int(xml.get("co2")), nox=int(xml.get("nox")), nh3=int(xml.get("nh3"))).save()

    def delete(self):
        Point.objects.all().get(id=self.id).delete()
    
    def view(self):
        data = Point.objects.all().get(id=self.id)
        return data
        
    def points_filter(self):
        self.add()
        points = Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))
        return points 
    
    def context(self):
        data = {"data":{"points":self.points_filter(), "center":self.points_filter()[0]}}
        return data

def compare(id):
    pass
