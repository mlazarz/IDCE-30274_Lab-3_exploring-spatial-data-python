# Author:  Mitchell Lazarz
# Python 2.7 -- Lab3_shape_exists.py
# Creation Date: 30 October 2020
# Description:  This script checks the Lab 3 data folder on the local drive to determine if cities.shp
# exists in the folder. A boolean output is printed to tell the user if the shapefile exists.  

# The arcpy module is imported.
import arcpy

# The geoprocessing environments are imported.
from arcpy import env

# The workspace environment is set to data folder on the local drive.
env.workspace='C://CLARK//PythonProgramming//CompProg_Lab3//Data-Lab_3_Exploring_Spatial_Data'

# Exists function is run to determine if cities.shp is within the workspace folder
shape_exists=arcpy.Exists("CITIES.SHP")

# The boolean output is printed. If True, cities.shp is in the folder. If false, cities.shp does not exist.
print(shape_exists)
