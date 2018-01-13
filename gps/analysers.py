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

class Pie_chart(object):
    def __init__(self):
        self.tree = etree.parse(xml_file)

    def extract_ppm(self):
        pass

        
