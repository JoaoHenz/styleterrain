from PIL import Image
from tools.biomedata import *



tag = 'watermap'

BLUE = (0,0,255)
# info = 'water_height'

#---CONFIGURATION------------------------------
width = 256
height = 256
biome = 'BForest'
path_data = 'output/heightmap.tif'
path_export = 'output/'
#----------------------------------------------

def createWaterMap(water_height):
    img_initial = Image.open(path_data)
    box = (0, 0, 0+width, 0+height)
    a = img_initial.crop(box)
    img_final=Image.new('RGB', (height,width), 255)
    img_final.paste(a)
    pixelmap = img_final.load()

    max_height = 0
    min_height = 255
    for i in range(0,height):
        for j in range(0,width):
            if img_initial.getpixel((i, j))[0] < min_height:
                min_height = img_initial.getpixel((i, j))[0]
            if img_initial.getpixel((i, j))[0] > max_height:
                max_height = img_initial.getpixel((i, j))[0]


    threshhold = (max_height - min_height) * water_height

    for i in range(0,height):
        for j in range(0,width):
            if img_initial.getpixel((i, j))[0] < threshhold:
                pixelmap[i,j] = BLUE
            else:
                pixelmap[i,j] = img_initial.getpixel((i, j))


    # img_initial.show()
    # img_final.show()
    img_final.save(path_export+"%s.tif" % (tag))
    print("salvamos a imagem "+"%s.tif" % (tag))
