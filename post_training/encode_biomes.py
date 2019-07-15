'''
SECOND

Encodes a latent for every image in the sample folder and show how that image is represented in the model

'''


import pickle
from stylegan_encoder.encode_images import encode_image
import dnnlib as dnnlib
import dnnlib.tflib as tflib
import os
from stylegan_encoder.encoder.generator_model import Generator
from stylegan_encoder.encoder.perceptual_model import PerceptualModel

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
iterations = 1000 #default = 1000

path = '../../dados_refinado/biohm_separado/'
direction = []   #latents which represent the direction of the biome in the latent representation of the generator network
#path_network = '../00026-sgan-bioheightmap-2gpu/network-snapshot-004085.pkl'
#path_network = '../../networks/network-snapshot-002500.pkl'
path_network = '../../networks/network-snapshot-009246.pkl'


################################################################################


tflib.init_tf()
with open(path_network,'rb') as f:
    generator_network, discriminator_network, Gs_network = pickle.load(f)

generator = Generator(Gs_network, 1, randomize_noise=False)
perceptual_model = PerceptualModel(256, layer=9, batch_size=1)
perceptual_model.build_perceptual_model(generator.generated_image)

for biomecolor in biomecolors:
    print('Bioma é ',biomecolor[1])
    path_biome = path + biomecolor[1]+ '/'
    biohm_encode = encode_image(path_biome+'source', path_biome+'generated', path_biome+'dlatent',path_network,iterations,generator_network, discriminator_network, Gs_network,generator,perceptual_model)
