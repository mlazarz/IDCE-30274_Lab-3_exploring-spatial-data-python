# Author:  Mitchell Lazarz
# Python 2.7 -- Lab3_listcopy.py
# Creation Date: 03 November 2020
# Description: This code creates a list of fields from the cities shapefile attributes and
# prints the field name and field type.

# The arcpy module is imported
import arcpy

# The geoprocessing environments are imported
from arcpy import env

# This allows output to overwrite files with same name
env.overwriteOutput = True

# The environment workspace is set to the Lab 3 data folder on the local drive
env.workspace = "C:/CLARK/PythonProgramming/CompProg_Lab3/Data-Lab_3_Exploring_Spatial_Data"

# A variable fieldlist is assigned to a list of field properties of the cities shapefile
fieldlist = arcpy.ListFields("cities.shp")

# A for loop is created that prints the field name and field type of all fields in the field list
for field in fieldlist: 
    print (field.name + " " + field.type)

# The following is the output
'''
FID OID
Shape Geometry
CITIESX020 Double
FEATURE String
NAME String
POP_RANGE String
POP_2000 Integer
FIPS55 String
COUNTY String
FIPS String
STATE String
STATE_FIPS String
DISPLAY SmallInteger
'''
    
