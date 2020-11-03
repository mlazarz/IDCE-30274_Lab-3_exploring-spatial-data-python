# Author:  Mitchell Lazarz
# Python 2.7 -- Lab3_list.py
# Creation Date: 03 November 2020
# Description:  The feature classes within the Lab 3 data folder are assigned to a
# list and the name and data type of each feature class in the list is printed.

# The arcpy module is imported
import arcpy

# The geoprocessing environments is imported
from arcpy import env

# The environment workspace is set to the Lab 3 data folder on the local drive
env.workspace = "C://CLARK//PythonProgramming//CompProg_Lab3//Data-Lab_3_Exploring_Spatial_Data"

# The variable fclist is assigned to a list of feature classes within the workspace folder
fclist = arcpy.ListFeatureClasses()
print(fclist)

# A for loop is created to print the name and dataType of feature classes within fclist
for fc in fclist: # for feature class in fclist
    fcdescribe = arcpy.Describe(fc) # The feature class properties are assigned to fcdescribe using the Describe module 
    print ('Name: ' + fcdescribe.name) # The name of the feature class is printed
    print ('Data type: ' + fcdescribe.dataType) # The data type of the feature class is printed


# The following is the output of the for loop
'''
Name: amtrak_stations.shp
Data type: ShapeFile
Name: cities.shp
Data type: ShapeFile
Name: counties.shp
Data type: ShapeFile
Name: new_mexico.shp
Data type: ShapeFile
Name: railroads.shp
Data type: ShapeFile
'''
