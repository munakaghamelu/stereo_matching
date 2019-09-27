# Librairies
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Function to transform a RGB image into a grayscale image
def rgb2gray(image_rgb):
    if len(image_rgb.shape)==3:
        image_gray = 0.2989*image_rgb[:,:,0]+0.5870*image_rgb[:,:,1]+0.1140*image_rgb[:,:,2]
    else:
        image_gray = image_rgb
    if np.max(image_gray)<1:
        image_gray = image_gray*255.
    return image_gray

if __name__=='__main__':
    path = 'Pair 1/'
    name_img1 = 'view1.png' # Image 1 of the stereo pair
    name_img2 = 'view2.png' # Image 2 of the stereo pair
    gt_img1 = 'disp1.png' # Ground truth 1
    gt_img2 = 'disp2.png' # Ground truth 2
    # Image 1
    img1 = mpimg.imread(os.path.join(path,name_img1))
    gt1 = mpimg.imread(os.path.join(path,gt_img1))
    # Image 2
    img2 = mpimg.imread(os.path.join(path,name_img2))
    gt2 = mpimg.imread(os.path.join(path,gt_img2))

    img1 = rgb2gray(img1)
    img2 = rgb2gray(img2)
    assert img1.shape == img2.shape, 'The two images should have the same size'

    # Showing the images
    if np.max(img1) > 1:
        im1show = img1.astype(float)/255.
        im2show = img2.astype(float)/255.
    else:
        im1show = img1
        im2show = img2
    f, axes = plt.subplots(2,2)
    axes[0,0].imshow(im1show, cmap='gray', interpolation='nearest', aspect=1)
    axes[0,0].axis('off')
    axes[0,0].set_title("Image 1 of the stereo pair")
    axes[0,1].imshow(im2show, cmap='gray', interpolation='nearest', aspect=1)
    axes[0,1].axis('off')
    axes[0,1].set_title("Image 2 of the stereo pair")
    axes[1,0].imshow(gt1, cmap='gray', interpolation='nearest', aspect=1)
    axes[1,0].axis('off')
    axes[1,0].set_title("Disparity map for image 1")
    axes[1,1].imshow(gt2, cmap='gray', interpolation='nearest', aspect=1)
    axes[1,1].axis('off')
    axes[1,1].set_title("Disparity map for image 2")
    plt.show()
