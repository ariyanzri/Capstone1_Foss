import cv2
import os

list_files = os.listdir('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/')

cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 500,500)

for f in list_files:
  image = cv2.imread('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f))
  cv2.imshow('Image',image)
  r = cv2.waitKey(0)
  print(r)
  
