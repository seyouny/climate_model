# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:07:53 2019

@author: jranders
"""

import matplotlib.pyplot as py
import numpy as np

import cartopy
import cartopy.feature as cfeature

filename = "VIIRSdata.csv"
filedata = np.loadtxt(filename, skiprows = 1, delimiter = ",")
lat = filedata[:,0]
lon = filedata[:,1]
frp = filedata[:,2]

py.close(1)
fig1 = py.figure(1, figsize =(8,6))
ax = fig1.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.scatter(lon,lat, color = "r")
ax.coastlines()
ax.gridlines()
ax.stock_img()

py.close(2)
fig2 = py.figure(2, figsize =(8,6))
ax = fig2.add_subplot(111, projection = cartopy.crs.Robinson())
ax.scatter(lon,lat, color = "r", transform = cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.stock_img()

py.close(3)
fig3 = py.figure(3, figsize =(8,6))
ax = fig3.add_subplot(111, projection = cartopy.crs.Robinson())
ax.scatter(lon,lat, c= frp, s = frp*3, cmap = py.cm.jet, marker ="+", transform = cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()


py.close(4)
fig4 = py.figure(4, figsize =(8,6))
states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
ax = fig4.add_subplot(111, projection=cartopy.crs.LambertConformal())
ax.set_extent([-125, -66.5, 20, 50], cartopy.crs.Geodetic())
ax.scatter(lon,lat, c= frp, s = frp*3, cmap = py.cm.jet, marker ="+", transform = cartopy.crs.PlateCarree())
ax.add_feature(states_provinces, edgecolor='gray')
ax.add_feature(cfeature.BORDERS)
ax.coastlines()
ax.gridlines()
ax.stock_img()
ax.set_title("Last 48 hours fire detections from VIIRS")
fig4.savefig('demo.png', bbox_inches='tight')


