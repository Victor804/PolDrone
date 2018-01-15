from lxml import etree

def extract_xml_to_maps(xml_file):
    tree = etree.parse(xml_file)
    flightcoodinates = []
    for coordinates in tree.xpath("/trkseg/trkpt"):
        latitude = coordinates.get("lat")
        longitude = coordinates.get("lon")
        latitude = (latitude[0:2]+"."+latitude[2:])
        longitude = (longitude[0:1]+"."+longitude[1:])
        flightcoodinates.append("{"+"lat:{0}, lng:{1}".format(latitude, longitude)+"},")
    
    center = flightcoodinates[0][:-1]
    flightcoodinates = "".join(flightcoodinates)
    gpsdata = {"gpsdata":{"center": center, "flightcoodinates": flightcoodinates}}
    return gpsdata

class Charts(object):
    def __init__(self, xml_file):
        self.tree = etree.parse(xml_file)
        
    def curve_chart(self):
        data = [['time', 'CO2', 'NH3', 'NOx']]
        for point in self.tree.xpath("/trkseg/trkpt/gaz"):
            data.append([point.get("time"), int(point.get("co2")), int(point.get("nh3")), int(point.get("nox"))])
        return data