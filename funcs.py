from PIL import Image
from PIL import ImageChops
folder1="/home/runner/compare-photos/Brora"
folder2="/home/runner/compare-photos/Brora2"

files1=os.listdir(folder1)
files2=os.listdir(folder2)
for file in files1:
  print (file)
  