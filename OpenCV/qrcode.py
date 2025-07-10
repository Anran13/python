# create qrcode
# package qucode

#============================================================
# one dimension
#============================================================
import qrcode
import qrcode.constants

# data = 'https://traffic.tbkc.gov.tw/'
data = 'Hellow~'
img = qrcode.make(data)
img.show()
img.save('qrcode.png')


#================================================
qr = qrcode.QRCode(version=10, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
# img = qr.make_image(fill_color = 'yellow') # NOT WORK under this env!
img.save('qrcode2.png')

#================================================
import qrcode
from qrcode.image.styledpil import StyledPilImage

data = 'https://github.com/opencv'

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save('qrcode3.png')

#================================================
img = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
img.save('qrcode4.png') 

img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255,255,255),(255,0,0),(0,0,255)), module_drawer=RoundedModuleDrawer())
img.save('qrcode5.png')

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path='image/python.png')
img.save('qrcode6.png')

import matplotlib.pyplot as plt
emb_img = cv2.imread('image/python.png')
height, width = emb_img.shape[:2]
center = (width/2, height/2)
rotationMatrix = cv2.getRotationMatrix2D(center,45,1)
rotated = cv2.warpAffine(emb_img, rotationMatrix,(height, width)) 
plt.figure(figsize=(10, 10))

cv2.imwrite("C:/Users/ROG/Desktop/PYImage_250621/image/python_rotated.png", rotated)

cv2.imshow('image', rotated)
cv2.waitKey(0)

#================================================
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer,RoundedModuleDrawer,HorizontalBarsDrawer,SquareModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask, HorizontalGradiantColorMask, ImageColorMask
from qrcode.image.styledpil import StyledPilImage

data = 'https://github.com/opencv'

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path='image/python_rotated.png', color_mask=HorizontalGradiantColorMask((255,255,255),(0,0,255),(255,255,0)), module_drawer=RoundedModuleDrawer())
img.save('qrcode7.png')