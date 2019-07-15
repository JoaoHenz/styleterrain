import os
import pickle
import numpy as np
from PIL import Image
import dnnlib as dnnlib
import dnnlib.tflib as tflib


tag = 'imagemtcc'
#---CONFIGURATION------------------------------
coarse_styles = (0,4)
middle_styles = (4,8)
fine_styles = (8,14)

path_network = 'data/networks/network-snapshot-006446.pkl'
# path_network = 'data/networks/network-snapshot-009246.pkl'
# coarse_biome = 'TSMBForest'
# middle_biome = 'BForest'
# fine_biome = 'Sea'

path_data = 'data/'
path_save = 'output/'
blackwhite = False

data_size = 256
synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8, resolution = data_size)
#----------------------------------------------

w= 256
h = 256
tflib.init_tf()
with open(path_network,'rb') as f:
    _G, _D, Gs = pickle.load(f)


biomes = ['TSMBForest','Tundra','Desert','Lake','MGrassland']

biome_latents = np.random.randn(5,14,512)
for i in range(0,5):
    biomel = np.load(path_data+'latent_reps/'+biomes[i]+'.npy')
    biome_latents[i] = biomel[0]

imgs = Gs.components.synthesis.run(biome_latents, randomize_noise=False, **synthesis_kwargs)

src_seeds = [91,388,9853,5643,701]

src_latents = np.stack(np.random.RandomState(seed).randn(Gs.input_shape[1]) for seed in src_seeds)
latents = Gs.components.mapping.run(src_latents, None) # [seed, layer, component]


imgs_2 = Gs.components.synthesis.run(latents, randomize_noise=False, **synthesis_kwargs)

width = w*6
height = h*6
bigimg = Image.new('RGB', (width,height), 'white')

for i in range(1,6):
    x1 = i*w
    y1 = 0
    x2 = i*w+w
    y2 = 0+h
    bigimg.paste(Image.fromarray(imgs[i-1], 'RGB'), (x1,y1,x2,y2))

for j in range(1,6):
    x1 = 0
    y1 = j*h
    x2 = 0+w
    y2 = j*h+h
    bigimg.paste(Image.fromarray(imgs_2[j-1], 'RGB'), (x1,y1,x2,y2))

count = 0
ii = 0
for i in range(w,width,w):
    jj = 0
    for j in range(h,height,h):
        latent = np.random.randn(1,14,512)
        latent[0] = latents[jj]
        # for k in range(middle_styles[0],middle_styles[1]):
        #     latent[0][k] = biome_latents[ii][k]
        for k in range(fine_styles[0],fine_styles[1]):
            latent[0][k] = biome_latents[ii][k]
        img = Gs.components.synthesis.run(latent, randomize_noise=False, **synthesis_kwargs)

        bigimg.paste(Image.fromarray(img[0], 'RGB'), (i,j,i+w,j+h))
        jj+=1
    ii+=1

if blackwhite:
    pixelmap = bigimg.load()
    for i in range(width):
        for j in range(height):
            pixelmap[i,j] = (pixelmap[i,j][0],pixelmap[i,j][1],pixelmap[i,j][0])

bigimg.save(path_save+tag+'.tif')
