from PIL import Image
from biomedata import *
import skimage
import matplotlib.pyplot as plt
from bitstring import Bits,BitArray
import numpy as np
import random
import sys

BLUE = (0,0,255)

#---CONFIGURATION------------------------------
path_height = 'output/heightmap.tif'
path_water = 'output/watermap.tif'
path_export = 'output/vegetationmaps/'

width = 256
height = 256
biome = 'Tundra'
info = ('trees_per_minitile','tree_den_var')
biome = 'TSMBForest'
tag = 'vegetationmap_big'

#----------------------------------------------

def onlyWater(m,n,img_water):
    for i in range(m,m+16):
        for j in range(n,n+16):
            if img_water.getpixel((i,j)) != BLUE: return False

    return True

def isWater(m,n,x,y,img_water):
    w_pos = (m+int(x/200),n+int(y/200))
    if img_water.getpixel(w_pos) == BLUE:
        return True
    else:
        return False


img_height = Image.open(path_height)
img_water = Image.open(path_water)
bin_sides = 3200
bin_size = bin_sides**2
mini_factor = 16


for m in range(0,256,16):                  #create one vegetation map for each tile
    for n in range(0,256,16):

        data = biomedata[biome]
        trees_per_minitile = data[info[0]]
        tree_den_var = data[info[1]]
        variation = random.uniform(-tree_den_var/2, tree_den_var/2)

        trees_per_minitile = trees_per_minitile + trees_per_minitile*variation
        trees_per_minitile = int(trees_per_minitile)


        bin_veg = BitArray('0b0' *bin_size )

        if not(onlyWater(m,n,img_water)):
            indices = np.random.randint(0, high=bin_size, size=trees_per_minitile)

            count = 0
            for i in range(0,len(indices)):
                if not(isWater(m,n,int(indices[i]/bin_sides),indices[i]%bin_sides,img_water)):
                    count +=1
                    bin_veg[indices[i]] = '0b1'

        print('')
        print('salvando '+path_export+tag+'_'+str(m)+'_'+str(n)+'.bin')
        f = open(path_export+tag+'_'+str(m)+'_'+str(n)+'.bin', 'wb')
        Bits(bin_veg).tofile(f)
