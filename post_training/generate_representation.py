'''
THIRD

Creates a latent representation for every biome based on the representations created for the sample images

'''


import pickle
import os
import random
from shutil import copyfile
import numpy as np
import dnnlib as dnnlib
import dnnlib.tflib as tflib
from stylegan_encoder.encode_images import encode_image
from stylegan_encoder.encoder.generator_model import Generator
from PIL import Image

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
alpha = 0.3
synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8)
#path_network = '../../networks/network-snapshot-002500.pkl'
path_network = '../../networks/network-snapshot-009246.pkl'


################################################################################



tflib.init_tf()
with open(path_network,'rb') as f:
    generator_network, discriminator_network, Gs_network = pickle.load(f)
generator = Generator(Gs_network, 1, randomize_noise=False)


for biomecolor in biomecolors:
    print('Bioma é ',biomecolor[1])
    path_biome = path + biomecolor[1]+ '/'

    dlatents = list(file for file in os.listdir(path_biome+'dlatent/') if os.path.splitext(file)[1] == '.npy')

    representation = np.load(path_biome+'dlatent/'+dlatents[0])

    for dlatent_file in dlatents:
        dlatent = np.load(path_biome+'dlatent/'+dlatent_file)
        for j in range(0,len(representation)):
            for k in range(0,len(representation[0])):
                representation[j][k] = representation[j][k] + alpha*(dlatent[j][k] - representation[j][k])
    try:os.mkdir(path_biome+'rep')
    except:print()


    representation = np.array([representation])
    generator.set_dlatents(representation)
    images = generator.generate_images()

    bioimage = Image.new('RGB', (256,256), 'white')
    bioimage.paste(Image.fromarray(images[0], 'RGB'))
    bioimage.save(path_biome+'rep/rep_image.tif')

    np.save(path_biome+'rep/representation.npy',representation)
