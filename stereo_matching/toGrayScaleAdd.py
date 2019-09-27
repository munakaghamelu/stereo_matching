import os
import numpy as np
import matplotlib.image as mpimg
from PIL import Image

def rgb2gray(image_rgb):
    if len(image_rgb.shape)==3:
        image_gray = 0.2989*image_rgb[:,:,0]+0.5870*image_rgb[:,:,1]+0.1140*image_rgb[:,:,2]
    else:
        image_gray = image_rgb
    if np.max(image_gray)<1:
        image_gray = image_gray*255.
    return image_gray

def getImg():
    #path = 'Pair 1/'
    name_img1 = 'view1.png'  # Image 1 of the stereo pair
    name_img2 = 'view2.png'  # Image 2 of the stereo pair
    # Image 1
    img1 = mpimg.imread(os.path.join(name_img1))
    # Image 2
    img2 = mpimg.imread(os.path.join(name_img2))

    img1 = rgb2gray(img1)
    im = Image.fromarray(img1)
    im = im.convert('L')
    im.save('view1_gray.png')
    img2 = rgb2gray(img2)
    im = Image.fromarray(img2)
    im = im.convert('L')
    im.save('view2_gray.png')

    name_img1 = 'view1_gray.png'  # Image 1 of the stereo pair
    name_img2 = 'view2_gray.png'  # Image 2 of the stereo pair
    # Image 1
    img1 = mpimg.imread(os.path.join(name_img1))
    # Image 2
    img2 = mpimg.imread(os.path.join(name_img2))

    img1 = rgb2gray(img1)
    img2 = rgb2gray(img2)
    print("Okieee no problemaaas !!")
    return img1, img2
