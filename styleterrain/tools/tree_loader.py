import bpy
import os
from bitstring import Bits,BitArray
from mathutils import Vector

path_vegmap = '../TCC/styleterrain/output/vegetationmaps/vegetationmap_big_128_128.bin'
number = 0
max_objects = 10000 *(number+1)
begin_at = number*10000
x = 128-128
y = 128-128
trees_per_tile = 100 #3200
pixel_per_tile = 16
factor = pixel_per_tile / trees_per_tile
 
f = open(path_vegmap, 'rb')
vegetationmap = f.read()
vegetationmap = BitArray(vegetationmap)
name_collection = 'Collection '+str(number+2)
collection = bpy.context.scene.collection.children[name_collection]


'''
for tree in collection.objects:
    bpy.data.objects[tree.name].select_set(True)
    if tree.name != 'Tree_Base':
        bpy.ops.object.delete() '''


tree_base = bpy.data.objects.get('Tree_Base')
map = bpy.data.objects.get('Map')



i = begin_at
while i<len(vegetationmap) and i<max_objects:
    if vegetationmap[i]:
        tree = tree_base.copy()
        collection.objects.link(tree)
        xa = int(i/trees_per_tile)
        ya = i%trees_per_tile
        xa = x + xa * factor
        ya = y + ya * factor
        tree.location = (xa,ya,20.0)    
        tree.name = 'tree_'+str(i)
        print(i, end = ' \r')
    i+=1
