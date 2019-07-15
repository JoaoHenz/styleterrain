'''
FOURTH

Exports the biome representations for use of the StyleTerrain tool

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
path = '../../dados_refinado/biohm_separado/'
path_toexport = '../styleterrain/data/latent_reps/'


################################################################################



for biomecolor in biomecolors:

    path_biome = path + biomecolor[1]+ '/'

    copyfile(path_biome+'rep/representation.npy',path_toexport+biomecolor[1]+'.npy')
