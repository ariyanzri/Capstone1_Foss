import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

list_files = os.listdir('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/')

for f in list_files:
  image = mpimg.imread('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f))
  plt.imshow(image)
  plt.show()
  
  
