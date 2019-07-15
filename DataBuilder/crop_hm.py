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
    im = Image.open(path_data)
    imgwidth, imgheight = im.size
    
    
    for i in range(0,imgheight,height):
      for j in range(0,imgwidth,width):
        if(k<maximages):
          if k > 3983:
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
              img=Image.new('RGB', (height,width), 255)
              img.paste(a)
              
              img.save(path+"%s.tif" % (tag+'_'+"{:06d}".format(k)))
              if(verbose): print("salvamos a imagem "+"%s.tif" % (tag+'_'+"{:06d}".format(k)) )
            except Exception as e: 
              if(verbose): print(e)
          k+=1
          
    print("salvou "+str(k)+" imagens!")



crop(path_cropados, path_hm+'heightmap.tif',256,256,99999999,"heightmap")

