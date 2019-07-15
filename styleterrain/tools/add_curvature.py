from PIL import Image
import math
import matplotlib.pyplot as plt
import numpy as np

tag = 'curvaturemap'

BLUE = (0,0,255)
# info = 'water_height'

#---CONFIGURATION------------------------------
width = 2501
height = 2501
biome = 'BForest'
path_data = 'output/heightmap.tif'
path_export = 'output/'
#----------------------------------------------


# img_initial = Image.open(path_data)
# img_final=Image.new('RGB', (height,width), 255)
#
# pixelmap = img_final.load()
#
# midpixel= (int(width/2)+1,int(width/2)+1)
#
# for i in range(width):
#     for j in range(height):
#         distance = math.sqrt( ((i-midpixel[0])**2)+((j-midpixel[1])**2) )
#         color = 255 - int(distance/5)
#         pixelmap[i,j] = (color,color,color)
#
#
#
# # img_initial.show()
# # img_final.show()
# img_final.save(path_export+"%s.tif" % (tag))
# print("salvamos a imagem "+"%s.tif" % (tag))

radius_earth = 6371*1.35449735
terrain = 256
limit = 3

def f(x): return np.sqrt(radius_earth**2-x**2)

 def f(x,y,z): return (x,y,np.sqrt(r**2-x**2-y**2))



plt.xlim(-limit/2, limit/2)
plt.ylim(6370-limit/2, 6370+limit/2)
plt.plot(t1, f(t1), )
plt.show()
