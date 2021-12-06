import os
import imageio
myfiles=os.listdir('tamrin')

images = []
for i in range(len(myfiles)):
    img = imageio.imread("images2"+myfiles[i])
    images.append(img)

imageio.mimsave('myfriends.gif', images)