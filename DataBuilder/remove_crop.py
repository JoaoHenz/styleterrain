from PIL import Image
import os
from imagedata import ImageData
import pickle

Image.MAX_IMAGE_PIXELS = 1000000000000


path_hm = '/media/jbmhenz/EXTERNOSOBR/dados_bruto/'
path_cropados = '/media/jbmhenz/EXTERNOSOBR/dados_refinado/heightmap/'
verbose = True


def crop(path, path_data, height, width,maximages,tag):
    k=0
    #im = Image.open(path_data)
    imgwidth = 43200
    imgheight = 21600
    count = 0
    
    for i in range(0,imgheight,height):
      for j in range(0,imgwidth,width):
        if(k<maximages):
          if j+width > imgwidth or i+height > imgheight:
            os.remove(path+"%s.tif" % (tag+'_'+"{:06d}".format(k)))
            if(verbose): print("deletamos a imagem "+"%s.tif" % (tag+'_'+"{:06d}".format(k)) )
            count+=1
        k +=1
    print("deletou "+str(count)+" imagens!")


crop(path_cropados, path_hm+'heightmap.tif',256,256,99999999,"heightmap")
