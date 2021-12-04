import os
import cv2
#import numpy as np
from imcompfunc import getfiles, diff

q=input("Search for duplicates in '1' folder, or search for copies in '2' folders - enter '1' or '2'")

#pa="c:/Users/brian/Pictures/sdcopy"
folder1="Brora"
folder2="Brora2"

#compare a folder for duplicates
#folder1=input("enter folder1")

#compare the images within folders 'Brora' and 'Brora2'
folder1=input("enter folder1")
folder2=input("enter folder2")

print ("checking "+folder1+" and "+folder2+" for differences")
#getfiles
