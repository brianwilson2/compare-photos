import os
import cv2
import tkinter as tk
import numpy as np
#from imcompfunc import getfiles, diff

#q=input("Search for duplicates in '1' folder, or search for copies in '2' folders - enter '1' or '2'")
#print (q)

#pa="c:/Users/brian/Pictures/sdcopy"
folder1="Brora"
folder2="Brora2"

cwd = os.getcwd()
print ("Home directory is:")
print (cwd)
##/home/runner/compare-photos

# Get the list of all files and directories
# in the root directory
path = cwd
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
# print the list
#print(dir_list)
#list folder contents
print ("start point")
for dir in dir_list:
  path=path+"/"+dir
  print (path)
  isdir=os.path.isdir(dir)
#  print (dir)
  if (isdir=="True"):
    print(dir)
    print(isdir)
    print ("/n")
#  print (file)
#compare a folder for duplicates
#folder1=input("enter folder1")

#compare the images within folders 'Brora' and 'Brora2'
#folder1=input("enter folder1")
#folder2=input("enter folder2")

#print ("checking "+folder1+" and "+folder2+" for differences")
#getfiles
