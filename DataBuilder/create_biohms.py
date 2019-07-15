from PIL import Image
import os
from imagedata import ImageData
import pickle

Image.MAX_IMAGE_PIXELS = 1000000000000


path_brutos = '/media/jbmhenz/EXTERNOSOBR/dados_bruto/'
path_cropados = '/media/jbmhenz/EXTERNOSOBR/dados_refinado/bioheightmap/'
path_hm = '/media/jbmhenz/EXTERNOSOBR/dados_refinado/heightmap/'
verbose = True
maximages = 99999999999999
height = 256
width = 256

blueheight = 21600
bluewidth = 43200
bluebiomemap = Image.open(path_brutos+'bluebiomemap.tif')
ko = 0
tag = 'bioheightmap'
count = 0


for i in range(0,blueheight,height):
  for j in range(0,bluewidth,width):
    if(count<maximages):
      if ko> 2693:
        if os.path.isfile(path_hm+"%s.tif" % ('heightmap'+'_'+"{:06d}".format(ko))):  #se existe um heightmap correspondente, criar bioheightmap  
          #print('vamos usar o')
          #print('i é '+str(i)+' e o j é '+str(j))
          #print("%s.tif" % ('heightmap'+'_'+"{:06d}".format(ko)))
          count += 1
          hm = Image.open(path_hm+"%s.tif" % ('heightmap'+'_'+"{:06d}".format(ko)))
          img=Image.new('RGB', (height,width), 255)
          img_pixelmap = img.load()
          box = (j, i, j+width, i+height)
          a = bluebiomemap.crop(box)
          img_a=Image.new('RGB', (height,width), 255)
          img_a.paste(a)
          #print('2')
          for k in range(0,height):
            for l in range(0,width):
              if img_a.getpixel((k, l)) != (255,255,255):
                img_pixelmap[k,l] = (hm.getpixel((k, l))[0],hm.getpixel((k, l))[1],img_a.getpixel((k, l))[2])
              else:
                #print('era branco')
                img_pixelmap[k,l] = hm.getpixel((k,l))
          
          print('3')
          img.show()
          img.save(path_cropados+"%s.tif" % (tag+'_'+"{:06d}".format(ko)))
          if(verbose): print("salvamos a imagem "+"%s.tif" % (tag+'_'+"{:06d}".format(ko)) )

        #else:
          #print(path_hm+"%s.tif" % (tag+'_'+"{:06d}".format(ko)))
      ko+=1
