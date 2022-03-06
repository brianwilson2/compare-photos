import numpy as np
from numpy import sum
def mse(imageA, imageB):
  print ("in funcs")
  print (imageA)
  print (imageB)
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err = float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

#folder1="/home/runner/compare-photos/Brora"
#folder2="/home/runner/compare-photos/Brora2"

#files1=os.listdir(folder1)
#files2=os.listdir(folder2)
#for file1 in files1:
#  print (file1)

#for file2 in files2:
#  print(file2)

