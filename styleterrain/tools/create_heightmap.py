import os
import pickle
import numpy as np
from PIL import Image
import dnnlib as dnnlib
import dnnlib.tflib as tflib

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

tag = 'heightmap'
tag_initial = 'heightmap_initial'

#---CONFIGURATION------------------------------
coarse_styles = (0,4)
middle_styles = (4,8)
fine_styles = (8,14)

path_network = 'data/networks/network-snapshot-006446.pkl'

# coarse_biome = 'TSMBForest'
# middle_biome = 'BForest'
# fine_biome = 'Sea'

path_data = 'data/'
path_save = 'output/'


data_size = 256
synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8, resolution = data_size)
#----------------------------------------------

tflib.init_tf()
with open(path_network,'rb') as f:
    _G, _D, Gs = pickle.load(f)


def createHM_SM(coarse_biome,middle_biome,fine_biome):
    coarse_biome = np.load(path_data+'latent_reps/'+coarse_biome+'.npy')
    middle_biome = np.load(path_data+'latent_reps/'+middle_biome+'.npy')
    fine_biome = np.load(path_data+'latent_reps/'+fine_biome+'.npy')

    latent = np.random.randn(1,14,512)

    for i in range(coarse_styles[0],coarse_styles[1]):
        latent[0][i] = coarse_biome[0][i]
    for i in range(middle_styles[0],middle_styles[1]):
        latent[0][i] = middle_biome[0][i]
    for i in range(fine_styles[0],fine_styles[1]):
        latent[0][i] = fine_biome[0][i]

    tflib.init_tf()
    with open(path_network,'rb') as f:
        _G, _D, Gs = pickle.load(f)

    image = Gs.components.synthesis.run(latent, randomize_noise=True, **synthesis_kwargs)
    image = image[0]

    bioimage = Image.new('RGB', (data_size,data_size), 'white')
    bioimage.paste(Image.fromarray(image, 'RGB'))
    pixelmap = bioimage.load()

    for i in range(0,data_size):
        for j in range(0,data_size):
            pixelmap[i,j] = (bioimage.getpixel((i,j))[0],bioimage.getpixel((i,j))[1],bioimage.getpixel((i,j))[1])

    # bioimage.show()
    bioimage.save(path_save+tag+'.tif')


def createHM_BO(biome,seed=None):
    biome = np.load(path_data+'latent_reps/'+biome+'.npy')


    if seed:
        latent = np.random.RandomState(1614).randn(1,14,512)
    else:
        latent = np.random.randn(1,14,512)


    image = Gs.components.synthesis.run(latent, randomize_noise=True, **synthesis_kwargs)
    image = image[0]

    bioimage = Image.new('RGB', (data_size,data_size), 'white')
    bioimage.paste(Image.fromarray(image, 'RGB'))
    pixelmap = bioimage.load()

    for i in range(0,data_size):
        for j in range(0,data_size):
            pixelmap[i,j] = (bioimage.getpixel((i,j))[0],bioimage.getpixel((i,j))[1],bioimage.getpixel((i,j))[1])

    # bioimage.show()
    bioimage.save(path_save+tag_initial+'.tif')


    for i in range(middle_styles[0],middle_styles[1]):
        latent[0][i] = biome[0][i]
    for i in range(fine_styles[0],fine_styles[1]):
        latent[0][i] = biome[0][i]

    image = Gs.components.synthesis.run(latent, randomize_noise=True, **synthesis_kwargs)
    image = image[0]

    bioimage = Image.new('RGB', (data_size,data_size), 'white')
    bioimage.paste(Image.fromarray(image, 'RGB'))
    pixelmap = bioimage.load()

    for i in range(0,data_size):
        for j in range(0,data_size):
            pixelmap[i,j] = (bioimage.getpixel((i,j))[0],bioimage.getpixel((i,j))[1],bioimage.getpixel((i,j))[1])

    # bioimage.show()
    bioimage.save(path_save+tag+'.tif')
