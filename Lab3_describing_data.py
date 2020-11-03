# Author:  Mitchell Lazarz
# Python 2.7 -- Lab3_describing_data.py
# Creation Date:  30 October 2020
# Description: This code uses the arcpy Describe function to display layer properties and information about shapefile of cities.

# A variable called myshape is assigned to the properties of a cities shapefile using the Describe function
myshape=arcpy.Describe("C://CLARK//PythonProgramming//CompProg_Lab3//Data-Lab_3_Exploring_Spatial_Data//cities.shp")

# This returns 'Shapefile' as cities datatype
myshape.dataType

# The cities shapefile is added to a .mxd manually
# A variable called mylayer is assigned to the properties of the cities.shp added to the .mxd
mylayer=arcpy.Describe("cities")

# This returns 'FeatureLayer' as mylayer data type
mylayer.dataType

# This returns 'FeatureClass' as mylayer dataset type
mylayer.datasetType

# This returns "C://CLARK//PythonProgramming//CompProg_Lab3//Data-Lab_3_Exploring_Spatial_Data//cities.shp" as the catalog path for mylayer
mylayer.catalogPath

# This returns 'cities' as the basename for mylayer
mylayer.basename

# This returns 'cities.shp' as the file name for mylayer
mylayer.file

# This indicates whether or not mylayer is versioned and returns a boolean output of False
mylayer.isVersioned

# This indicates the shape type of mylayer and returns 'Point'
mylayer.shapeType

# This indicates the spatial reference value of mylayer and returns 'geoprocessing spatial reference object object at 0x17F57A88'
mylayer.spatialReference

# This returns the name of the coordinate system of mylayer, 'GCS_North_American_1983'
mylayer.spatialReference.name

# This returns the type of coordinate system of mylayer, 'Geographic'
mylayer.spatialReference.type

# This indicates the largest and smallest x and y coordinates within mylayer and returns '-400 -400 400 400'
mylayer.spatialReference.domain

