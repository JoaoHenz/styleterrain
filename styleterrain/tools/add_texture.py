from PIL import Image
from tools.biomedata import *





BLUE = (0,0,255)


#---CONFIGURATION------------------------------
width = 256
height = 256
# biome = 'TSMBForest'
path_water = 'output/watermap.tif'
path_height = 'output/heightmap.tif'
path_export = 'output/'
tag = 'texturemap'

#----------------------------------------------

# t ={ #textures
#     'rock': (150,150,150),
#     'snowrock': (220,220,220),
#     'dryrock': (160,160,120),
#     'grass': (50,200,50),
#     'snowgrass': (100,200,100),
#     'drygrass': (150,200,50),
#     'wetgrass': (0,150,0),
#     'sand': (200,200,100),
#     'snow': (230,230,255),
#     'mud': (200,150,150),
#     'ice': (200,200,255),
#     'none': (0,0,0),
# }

t ={ #textures
    'rock': (150,150,150),
    'snowrock': (220,220,220),
    'dryrock': (160,160,120),
    'grass': (50,200,50),
    'snowgrass': (100,200,100),
    'drygrass': (150,200,50),
    'wetgrass': (0,150,0),
    'sand': (200,200,100),
    'snow': (230,230,255),
    'mud': (200,150,150),
    'ice': (200,200,255),
    'underwater': (0,0,255),
    'none': (0,0,0),
}
def heightDifference(x,y,img_height):
    height_pixel = img_height.getpixel((x,y))[0]
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i<width and j<height:
                height_op = img_height.getpixel((i,j))[0]
                if height_op *1.25 < height_pixel or height_op *0.75 > height_pixel:
                    return True
    return False

def addRock(pixel_map,img_water,img_height,biome):

    for i in range(0,width):
        for j in range(0,height):
            if img_water.getpixel((i,j))==BLUE:
                pixel_map[i,j] = t['underwater']
            elif heightDifference(i,j,img_height):
                if biomedata[biome]['temperature'] < 0.2:pixel_map[i,j] = t['snowrock']
                else:
                    if biomedata[biome]['humidity'] < 0.1:pixel_map[i,j] = t['dryrock']
                    else: pixel_map[i,j] = t['rock']

    return pixel_map

def addBase(pixel_map,biome):
    for i in range(0,width):
        for j in range(0,height):
            if pixel_map[i,j] ==t['none']:
                if biomedata[biome]['temperature'] < 0.1:pixel_map[i,j] = t['snow']
                else:
                    if biomedata[biome]['temperature'] < 0.2:pixel_map[i,j] = t['snowgrass']
                    else:
                        if biomedata[biome]['humidity'] > 0.9:pixel_map[i,j] = t['wetgrass']
                        else:
                            if biomedata[biome]['humidity'] > 0.5:pixel_map[i,j] = t['grass']
                            else:
                                if biomedata[biome]['temperature'] > 0.8:pixel_map[i,j] = t['sand']
                                else:
                                    pixel_map[i,j] = t['drygrass']
    return pixel_map

def addWaterEffect(pixel_map,img_water,biome):
    for i in range(0,width):
        for j in range(0,height):
            if img_water.getpixel((i,j)) == BLUE:
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if k<width and l<height:
                            change = ''
                            if pixel_map[k,l] == t['dryrock']: change = 'rock'
                            if pixel_map[k,l] == t['rock']: change = 'sand'
                            if pixel_map[k,l] == t['sand']: change = 'drygrass'
                            if pixel_map[k,l] == t['drygrass']: change = 'grass'
                            if pixel_map[k,l] == t['grass']: change = 'wetgrass'
                            if pixel_map[k,l] == t['wetgrass']: change = 'mud'
                            if pixel_map[k,l] == t['snow']: change = 'ice'
                            if change != '': pixel_map[k,l] = t[change]
    return pixel_map

def createTextureMap(biome):
    img_water = Image.open(path_water)
    img_height = Image.open(path_height)
    img_texture = Image.new('RGB', (height,width), t['none'])
    pixel_map = img_texture.load()
    print('adding rock...')
    pixel_map = addRock(pixel_map,img_water,img_height,biome)
    print('adding base...')
    pixel_map = addBase(pixel_map,biome)
    print('adding water effects...')
    pixel_map = addWaterEffect(pixel_map,img_water,biome)



    # img_texture.show()
    img_texture.save(path_export+"%s.tif" % (tag))
    print("salvamos a imagem "+"%s.tif" % (tag))
