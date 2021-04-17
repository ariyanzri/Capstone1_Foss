import cv2
import os
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
from PIL import Image
import piexif
import PIL.ExifTags

list_files = os.listdir('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/')

images = []

for f in list_files:
  img = Image.open('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f))
#   exif_dict = piexif.load(img.info['exif'])
#   print(exif_dict)
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

print(exif)

#   image = mpimg.imread('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f))
#   images.append(image)
#   images.append(cv2.imread('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f)))
#   im = Image.open('{0}/{1}'.format('/home/ariyanzarei/drone_data/2.27.20_P4_15m_RGB/',f))
#   images.append(im)
#   break
  
  
# cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Image', 500,500)
# cv2.imshow('Image',images[0])
# cv2.waitKey(0)
      
# plt.imshow(images[0])
# plt.show()  
  
# im.show()
  
