# -*- coding: utf-8 -*-


from PIL import Image
import os

biomecolors = [     
    (50,'TSMBForest'), 
    (59,'TSDBForest'), 
    (69,'TSCForest'), 
    (78,'PBMForest'),  
    
    (87,'PCForest'), 
    (97,'BForest'), 
    (106,'TSGrassland'),
    (116,'PGrassland'),  
    
    (125,'FGrassland'), 
    (134,'MGrassland'),   
    (144,'Tundra'),  
    (153,'DForest'),  
    
    (163,'Desert'),  
    (172,'Mangrove'),  
    (181,'Lake'),  
    (191,'RockIce'),  
    
    (0,'Sea'),
    ]

verbose = True
#     if(verbose): print()


class ImageData(object):      
  def __init__(self,path_biomemap,path_heightmap):
    biomemap = Image.open(path_biomemap)
    #heightmap = Image.open(path_heightmap)    
    
    biomecolors_count = []
    for i in range(0,len(biomecolors)):
      biomecolors_count.append(0)

    imgwidth, imgheight = biomemap.size
    
    for i in range(0,imgheight):
        for j in range(0,imgwidth):
          rgb = biomemap.getpixel((i, j))
          k=0
          while k<len(biomecolors) and biomecolors[k]!=rgb:
            k+=1
          if k<len(biomecolors) and biomecolors[k]==rgb:
            biomecolors_count[k]+=1
            
            
    #print(biomecolors_count)
    #imagesize = imgwidth*imgheight
    biomecolors_percent = []
    imagesize = sum(biomecolors_count)
    for i in range(0,len(biomecolors_count)):
      biomecolors_percent.append(biomecolors_count[i]/imagesize) 

    print_list = []
    if biomecolors_count[0]>0: print_list.append('TSMBForest')
    if biomecolors_count[1]>0: print_list.append('TSDBForest')
    if biomecolors_count[2]>0: print_list.append('TSCForest')
    if biomecolors_count[3]>0: print_list.append('PBMForest')
    if biomecolors_count[4]>0: print_list.append('PCForest')
    if biomecolors_count[5]>0: print_list.append('BForest')
    if biomecolors_count[6]>0: print_list.append('TSGrassland')
    if biomecolors_count[7]>0: print_list.append('PGrassland')
    if biomecolors_count[8]>0: print_list.append('FGrassland')
    if biomecolors_count[9]>0: print_list.append('MGrassland')
    if biomecolors_count[10]>0: print_list.append('Tundra')
    if biomecolors_count[11]>0: print_list.append('DForest')
    if biomecolors_count[12]>0: print_list.append('Desert')
    if biomecolors_count[13]>0: print_list.append('Mangrove')
    if biomecolors_count[14]>0: print_list.append('Lake')
    if biomecolors_count[15]>0: print_list.append('RockIce')
    if biomecolors_count[16]>0: print_list.append('Sea')
    
    #if(verbose): print(biomecolors_percent)
    print(print_list)

    self.biomedata = biomecolors_percent
    self.imagepath = path_heightmap

    print(self.imagepath)
    print('\n\n')

    '''
    self.TSMBForest = biomecolors_count[0]
    self.TSDBForest = biomecolors_count[1]
    self.TSCForest = biomecolors_count[2]
    self.PBMForest = biomecolors_count[3]
    self.PCForest = biomecolors_count[4]
    self.BForest = biomecolors_count[5]
    self.TSGrassland = biomecolors_count[6]
    self.PGrassland = biomecolors_count[7]
    self.FGrassland = biomecolors_count[8]
    self.MGrassland = biomecolors_count[9]
    self.Tundra = biomecolors_count[10]
    self.DForest = biomecolors_count[11]
    self.Desert = biomecolors_count[12]
    self.Mangrove = biomecolors_count[13]
    self.Lake = biomecolors_count[14]
    self.RockIce = biomecolors_count[15]
    self.Sea = biomecolors_count[16]
    '''
    
    
  def limpainutil(path_biomemap,path_heightmap):
    biomemap = Image.open(path_biomemap)
    #heightmap = Image.open(path_heightmap)    
    
    biomecolors_count = []
    for i in range(0,len(biomecolors)):
      biomecolors_count.append(0)

    imgwidth, imgheight = biomemap.size
    
    for i in range(0,imgheight):
        for j in range(0,imgwidth):
          rgb = biomemap.getpixel((i, j))
          k=0
          while k<len(biomecolors) and biomecolors[k]!=rgb:
            k+=1
          if k<len(biomecolors) and biomecolors[k]==rgb:
            biomecolors_count[k]+=1
            if k!=16:
              return

    #print(biomecolors_count)
    imagesize = imgwidth*imgheight
    if biomecolors_count[16] == imagesize:
       if(verbose): 
         print('limpando inutil')
       os.remove(path_biomemap)
       os.remove(path_heightmap)

    if(verbose): print(biomecolors_count)

        
      
      
      
      
      
      
      
      
