# Author:  Mitchell Lazarz
# Python 2.7 -- Lab3_listcopy.py
# Creation Date: 03 November 2020
# Description:  This code creates a geodatabase and copies all feature classes within the Lab 3
# data folder into the geodatabase using the basename of the copied feature classes.

# The arcpy module is imported
import arcpy

# The geoprocessing environments is imported
from arcpy import env

# This allows output to overwrite files with same name
env.overwriteOutput = True

# The environment workspace is set to the Lab 3 data folder on the local drive
env.workspace = "C:/CLARK/PythonProgramming/CompProg_Lab3/Data-Lab_3_Exploring_Spatial_Data"

# A geodatabase, NM.gdb, is created in the Results folder
arcpy.CreateFileGDB_management("C:/CLARK/PythonProgramming/CompProg_Lab3/Data-Lab_3_Exploring_Spatial_Data/Results/","NM.gdb")

# The variable fclist is assigned to a list of feature classes within the workspace folder
fclist = arcpy.ListFeatureClasses()

# A for loop is created that copies all feature classes into the NM.gdb with the feature classes' basename
for fc in fclist: # for each feature class in the feature class list
    fcdesc = arcpy.Describe(fc) # Assign the feature class properties to the variable, fcdesc
    arcpy.CopyFeatures_management(fc, "C:/CLARK/PythonProgramming/CompProg_Lab3/Data-Lab_3_Exploring_Spatial_Data/Results/NM.gdb/" + fcdesc.basename) # Copy the feature class to the NM geodatabase with the basename from the feature class properties
    
