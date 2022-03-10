import numpy as np
from numpy import sum

def comp(image1,image2):
#  image2 = cv2.imread("dad3.jpg")
 # image1 = cv2.imread("dad1.jpg")

  difference = cv2.subtract(image1, image2)

  result = not np.any(difference)  #if diff is all '0' it will return false

  if result is True:
    print("the images are the same")
    p="True"
  else:
    cv2.imwrite("result.jpg", difference)
    print("the images are different")
    p="False"
  return p

#folder1="/home/runner/compare-photos/Brora"
#folder2="/home/runner/compare-photos/Brora2"

#files1=os.listdir(folder1)
#files2=os.listdir(folder2)
#for file1 in files1:
#  print (file1)

#for file2 in files2:
#  print(file2)
"""
def mse(imageA, imageB):
  print ("in funcs")
  print (imageA)
  print (imageB)
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float")-imageB.astype("float"))**2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
"""
