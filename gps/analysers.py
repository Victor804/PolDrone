from lxml import etree
from gps.models import Project, Flight, Point
from django.conf import settings

class Charts(object):
    def __init__(self, id):
        self.id = id
        
    def curve_chart(self):
        data = [['time', 'CO2', 'NH3', 'NOx']]
        points = Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))
        for point in points:
            data.append([(point.time).encode('utf-8'), point.c02, point.nh3, point.nox])
        print data
        return data
    
class Point_model(object):
    def __init__(self, id):
        self.id = id

    def add(self):        
        path_xml_file = Flight.objects.all().get(id=self.id).xml_file
        xml_file = (settings.MEDIA_ROOT + str(path_xml_file))
        tree = etree.parse(xml_file)
        if str(Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))) == "<QuerySet []>":
            for xml in tree.xpath("/trkseg/trkpt"):
                Point(flight=Flight.objects.all().get(id=self.id), lat=float(xml.get("lat")), lon=float(xml.get("lon")), time=xml.get("hour"), c02=int(xml.get("co2")), nox=int(xml.get("nox")), nh3=int(xml.get("nh3"))).save()

    def delete(self):
        Point.objects.all().get(id=self.id).delete()
    
    def view(self):
        data = Point.objects.all().get(id=self.id)
        return data
        
class Maps(object):
    def __init__(self, id):
        self.id = id
        self.point_model = Point_model(id)
        
    def points(self):
        self.point_model.add()
        points = Point.objects.all().filter(flight=Flight.objects.all().get(id=self.id))
        return points 
    
    def context(self):
        data = {"data":{"points":self.points, "center":self.points()[0]}}
        return data
