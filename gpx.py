#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:12:24 2017

@author: victor
"""

import gpxpy
import gpxpy.gpx

# Parsing an existing file:
# -------------------------

gpx_file = open('', 'r')

gpx = gpxpy.parse(gpx_file)
flighplancoordinates = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            flighplancoordinates.append('{'+'lat:{0}, lng:{1}'.format(point.latitude, point.longitude)+'},')

print flighplancoordinates
