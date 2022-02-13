from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import operator 

def image_to_binary(img):
 #code below is to convert image to binary

 R = img[:,:,0]
 G = img[:,:,1]
 B = img[:,:,2]
 binary = (R+G+B)/3

 for i in range(500):
    for j in range(500):
        if binary[i,j]>10:
                binary[i,j]=1
        else:
                binary[i,j]=0

 return binary


#read images
img_circle = mpimg.imread('circle.jpg')
img_rectangle = mpimg.imread('rectangle.jpg')

# now calling function to convert image in binary
binary_circle = image_to_binary(img_circle)
binary_rectangle = image_to_binary(img_rectangle)

#showing circle 
plt.imshow(binary_circle, cmap='gray')
plt.title('Circle',fontsize=24)
plt.show()
#showing rectangle
plt.imshow(binary_rectangle, cmap='gray')
plt.title('Rectangle',fontsize=24)
plt.show()
#logical and
img_and = binary_circle.astype(int) & binary_rectangle.astype(int)
plt.imshow(img_and, cmap='gray')
plt.title('Logical AND',fontsize=24)
plt.show()

#logical or
img_or = binary_circle.astype(int) | binary_rectangle.astype(int)
plt.imshow(img_or, cmap='gray')
plt.title('Logical OR',fontsize=24)
plt.show()

#logical xor
img_xor = binary_circle.astype(int) ^ binary_rectangle.astype(int)
plt.imshow(img_xor, cmap='gray')
plt.title('Logical XOR',fontsize=24)
plt.show()

#logical nand
img_nand = ~img_and
plt.imshow(img_nand, cmap='gray')
plt.title('Logical NAND',fontsize=24)
plt.show()

#logical nor
img_nor = ~img_or
plt.imshow(img_nor, cmap='gray')
plt.title('Logical NOR',fontsize=24)
plt.show()

#logical xnor
img_xnor = ~img_xor
plt.imshow(img_xnor, cmap='gray')
plt.title('Logical XNOR',fontsize=24)
plt.show()
