from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#read image
img = mpimg.imread('input.jpg')

#read the red, green and blue colourspaces differently
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

#display the red image
plt.imshow(R, cmap='Reds')
plt.title('Red Image',fontsize=24)
plt.show()

#display the green image
plt.imshow(G, cmap='Greens')
plt.title('Green Image',fontsize=24)
plt.show()

#display the blue image
plt.imshow(B, cmap='Blues')
plt.title('Blue Image',fontsize=24)
plt.show()