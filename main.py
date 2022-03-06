import os
import os.path
import cv2 as cv
import tkinter as tk
import numpy as np
from PIL import Image
from PIL import ImageChops
#from imcompfunc import getfiles, diff

#q=input("Search for duplicates in '1' folder, or search for copies in '2' folders - enter '1' or '2'")
#print (q)

#pa="c:/Users/brian/Pictures/sdcopy"
folder1="Brora"
folder2="Brora2"

cwd = os.getcwd()
print ("Home directory is:")
print (cwd)##/home/runner/compare-photos
path = cwd


# Get the list of all files and directories
# in the root directory

dir_list = os.listdir(path)
dirs=[]
#print("directories found in '", path, "' :")
#list folder contents
for file in dir_list:
  isdir=os.path.isdir(file)
  if (isdir==True) and (file.find("."))==-1:
    if (file.find("."))==-1:
   #   print(file, end=" ")
    #  print(isdir)
    #  print ("\n")
      pat=cwd+"/"+file
    #  print ("dir paths")
   #   print (pat)
      dirs.append(pat)
print ("dirs from here")

for dir in dirs:
  print ("directory listing for ")
  print (dir)
  files = os.listdir(dir)
  for file in files:
    print(file)
# list files within each directory
      
#compare a folder for duplicates
#folder1=input("enter folder1")

#compare the images within folders 'Brora' and 'Brora2'
#folder1=input("enter folder1")
#folder2=input("enter folder2")

#print ("checking "+folder1+" and "+folder2+" for differences")
#getfiles
