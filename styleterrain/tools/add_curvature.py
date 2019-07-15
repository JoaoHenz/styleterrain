import bpy
import math

def f(x,y,z): return (x,y,math.sqrt(r**2-x**2-y**2))


map = bpy.data.objects.get('Map')

mesh = map.data

for vertice in mesh.vertices:
    vertice.co = f(vertice.co.x,vertice.co.y,vertice.co.z)
    print('indo')