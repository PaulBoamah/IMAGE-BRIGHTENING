#import required libraries
from PIL import Image,ImageEnhance
import glob
import numpy as np

#read the lab images
file_list = glob.glob(
    r'Images\*.*'
)
#create list to store all image file paths
image_list = []
for file in file_list:
    image_list.append(file)
    

#image brightness enhancer
for im in image_list:
    #use string.split attribute to read actual filename
    image_split = im.split('\\')
    image_name = image_split[1]
    

    #load image for enhancement
    imo = Image.open(im)
    enhancer = ImageEnhance.Brightness(imo)
    factor = 1.5 #gives original image
    im_bright = enhancer.enhance(factor)
    

    #save brightened image to directory
    im_bright.save(image_name + '_brightened.jpg')

    #display old and new image
    Image.fromarray(np.hstack((np.array(imo),np.array(im_bright)))).show()

