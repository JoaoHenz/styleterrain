from PIL import Image
import os
from shutil import copyfile



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
#TSMBForest TSDBForest TSCForest PBMForest PCForest BForest TSGrassland PGrassland FGrassland MGrassland Tundra DForest Desert Mangrove Lake RockIce Sea

path = '../../dados_refinado/bioheightmap/'
path_final = '../../dados_refinado/biohm_separado/'

for file in os.listdir(path):
    im = Image.open(path+file)
    biome_counter = []
    for i in range(0,len(biomecolors)):
        biome_counter.append(0)
    imwidth, imheight = im.size
    half = imwidth * imheight /2

    done = False
    for i in range(0,imwidth):    #count how many pixels of each biome
        for j in range(0,imheight):
            if done ==False:
                achou = False
                k = 0
                while not(achou) and k<len(biomecolors):
                    if im.getpixel((i, j))[2] == biomecolors[k][0]:
                        achou = True
                        biome_counter[k]+= 1
                        if biome_counter[k] > half:
                            done = True
                    k+=1

    biggest = (0,'')
    for i in range(0,len(biome_counter)):
        if biome_counter[i] > biggest[0]:
            biggest = (biome_counter[i],biomecolors[i][1])

    copyfile(path+file, path_final+biggest[1]+'/'+file)
    print('salvamos o '+file)
