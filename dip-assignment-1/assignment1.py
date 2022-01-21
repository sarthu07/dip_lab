import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb_to_gray(img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img.copy()

        for i in range(3):
           grayImage[:,:,i] = Avg
           
        return grayImage       

image = mpimg.imread("yoyoy.jpg")   
grayImage = rgb_to_gray(image)  

img = np.array(grayImage)
binarr = np.where(img>128, 255, 0)

img3 = np. add(grayImage, binarr)

img4 = np.add(20,grayImage)


#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1,4) 
axarr[0].imshow(grayImage)
axarr[1].imshow(binarr, cmap='gray')
axarr[2].imshow(img3, cmap='gray')
axarr[3].imshow(img4 , cmap='gray')
plt.show()