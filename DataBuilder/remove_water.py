from PIL import Image
import os
from imagedata import ImageData
import pickle

Image.MAX_IMAGE_PIXELS = 1000000000000


path_hm = '/media/jbmhenz/EXTERNOSOBR/dados_bruto/'
path_cropados = '/media/jbmhenz/EXTERNOSOBR/dados_refinado/heightmap/'
verbose = True
max_water = 0.95


def removewater(path, height, width,maximages,tag):
    k=0
    im = Image.open(path)
    imgwidth, imgheight = im.size
    maxwaterpixels = max_water *(imgwidth*imgheight)
    count_water = 0
    mustfinish = False
    count = 0

    for i in range(0,imgheight):
      for j in range(0,imgwidth):
        if(k<maximages):
          if not(mustfinish):
            rgb = im.getpixel((i, j))
            if rgb == (0,0,0):
              count_water+=1

            if count_water > maxwaterpixels:
              os.remove(path)
              if(verbose): print("deletamos a imagem "+"%s" % path )
              mustfinish = True
              count+=1
        k +=1
  


for file in os.listdir(path_cropados):
  removewater(path_cropados+file,256,256,99999999,"heightmap")
