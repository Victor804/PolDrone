import gpxpy
import gpxpy.gpx 

def maps(gpx_file):
    gpx = gpxpy.parse(gpx_file)
    flightcoodinates = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                flightcoodinates.append("{"+"lat:{0}, lng:{1}".format(point.latitude, point.longitude)+"},")
    center = flightcoodinates[0][:-1]
    
    flightcoodinates = "".join(flightcoodinates)
    gpsdata = {"gpsdata":{"center": center, "flightcoodinates": flightcoodinates}}
    return gpsdata