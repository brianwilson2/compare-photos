import cv2
import numpy as np

image2 = cv2.imread("dad3.jpg")
image1 = cv2.imread("dad1.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)  #if diff is all '0' it will return false

if result is True:
    print("the images are the same")
else:
    cv2.imwrite("result.jpg", difference)
    print("the images are different")
