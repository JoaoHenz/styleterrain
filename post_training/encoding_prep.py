'''
FIRST

Deletes all files in the folders of every biome, and then samples 'num_source' images from every biome for the latent discovery


'''
import pickle
import os
import random
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
    #(172,'Mangrove'), #not enough data
    (181,'Lake'),
    (191,'RockIce'),

    (0,'Sea'),
    ]


# CONFIGURATION ###############################################################
num_source = 5
path = '../../dados_refinado/biohm_separado/'

################################################################################

for biomecolor in biomecolors:

    path_biome = path + biomecolor[1]+ '/'
    for file in os.listdir(path_biome+"source/"):
        os.remove(path_biome+"source/"+file)
    try:
        for file in os.listdir(path_biome+"generated/"):
            os.remove(path_biome+"generated/"+file)
        for file in os.listdir(path_biome+"dlatent/"):
            os.remove(path_biome+"dlatent/"+file)
    except:
        print('')
    biohms = list(file for file in os.listdir(path_biome) if os.path.splitext(file)[1] == '.tif')
    new_source = random.sample(biohms,num_source)
    for biohm in new_source:
        copyfile(path_biome+biohm,path_biome+'source/'+biohm)
