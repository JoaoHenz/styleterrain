# -*- coding: utf-8 -*-

from PIL import Image
import os
from imagedata import ImageData
import pickle

Image.MAX_IMAGE_PIXELS = 1000000000000  
verbose = True
  

def crop(path, path_data, height, width,maximages,tag):
    k=0
    im = Image.open(path_data)
    imgwidth, imgheight = im.size
    
    
    for i in range(0,imgheight,height):
      for j in range(0,imgwidth,width):
        if(k<maximages):
          if k>3983:
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
    
    
    
def cleanfolder(folder):
  for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        if(verbose): print(e)


def test_results():
  file = open(path_final+"imagedescriptor.txt","rb")
  result_list = pickle.load(file)
  for i in range(0,len(result_list)):
    print(result_list[i].biomedata)

'''
nomearquivo  porcentagens
1.tif PCForest 0.3 MGrassland 0.4 Sea 0.3

'''

path_initial = 'C:\\users\\joaohenz\\Desktop\\TCC\\dados_bruto\\'
path_final = 'C:\\users\\joaohenz\\Desktop\\TCC\\dados\\'
path_final_biomemaps = 'C:\\users\\joaohenz\\Desktop\\TCC\\dados\\biomemaps\\'
path_final_heightmaps = 'C:\\users\\joaohenz\\Desktop\\TCC\\dados\\heightmaps\\'
path = 'C:\\users\\joaohenz\\Desktop\\TCC\\Dados\\'
path_sem_compressao = 'C:\\users\\joaohenz\\Desktop\\TCC\\Dados_sem_compressao\\'
path_biomemap = path_initial+"biomemap.tif"
path_heightmap = path_initial+"heightmap.tif"

'''
if(verbose): print('\n\n##########Limpando Pastas!\n#############################################')
cleanfolder(path_final)
cleanfolder(path_final_biomemaps)
cleanfolder(path_final_heightmaps)

if(verbose): print('\n\n##########Cortando Imagens!\n#############################################')
imagelimit = 999999999999 #16 999999999999
crop(path_final_biomemaps, path_biomemap,540,540,imagelimit,"biomemap")
crop(path_final_heightmaps, path_heightmap,540,540,imagelimit,"heightmap")

if(verbose): print('\n\n##########Limpando Inúteis!\n#############################################')
for filename in os.listdir(path_final_biomemaps):
  filename = os.path.splitext(filename)[0]
  filename = filename.split('_')
  ImageData.limpainutil(path_final_biomemaps+'biomemap_'+filename[1]+'.tif',path_final_heightmaps+'heightmap_'+filename[1]+'.tif')
'''

if(verbose): print('\n\n##########Gerando Descriptor!\n#############################################')
imagedata_list = []
descriptor = open(path_final+"imagedescriptor.txt","wb")
descriptor.truncate(0)

for filename in os.listdir(path_final_biomemaps):
  filename = os.path.splitext(filename)[0]
  filename = filename.split('_')
  imagedata = ImageData(path_final_biomemaps+'biomemap_'+filename[1]+'.tif',path_final_heightmaps+'heightmap_'+filename[1]+'.tif')
  imagedata_list.append(imagedata)
  #if(verbose): print(imagedata.biomedata)
  
if(verbose): print('\n\n##########Salvando Descriptor!\n#############################################')
pickle.dump(imagedata_list,descriptor)
descriptor.close()
if(verbose): print('foram salvos '+str(len(imagedata_list))+' dados!')
if(verbose): print('\n\n##########Fim de Execução!\n#############################################')











