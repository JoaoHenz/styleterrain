



import pickle
#from imagedata import ImageData




def decrease_sea(imagedata_list):
  '''
  decreases the quantity of sea infested tiles by eliminating tiles with more than
  a customized maximum sea presence
  
  '''
  
  maximum_sea_presence = 0.95
  new_imlist = []
  
  for i in range(0,len(imagedata_list)):
    if imagedata_list[i].biomedata[16] < maximum_sea_presence:
      new_imlist.append(imagedata_list[i])

  return new_imlist








path_final = 'C:\\users\\joaohenz\\Desktop\\TCC\\dados\\'
imagedata_list = []

file = open(path_final+"imagedescriptor.txt",'rb')

imagedata_list = pickle.load(file)

'''
'TSMBForest':[255,0,4], ok
'TSDBForest':[228,69,2], ok
'TSCForest':[201,138,1],  ok
'PBMForest':[177,159,20],  ok

'PCForest':[160,88,79],  ok
'BForest':[142,18,138],  ok
'TSGrassland':[105,54,147], ok
'PGrassland':[60,126,140], ok 

'FGrassland':[15,198,133], ok
'MGrassland':[2,171,156], ok
'Tundra':[5,93,196], ok
'DForest':[8,14,236], ok  

'Desert':[5,81,244],   ok
'Mangrove':[2,179,246], ok
'Lake':[0,238,204],   ok
'RockIce':[0,247,102],   ok

'Sea':[255,255,255],  ok
 
'''
print('\n\n')
#print(imagedata_list[0].biomedata)
    

print('Quantidade de dados: %d \n\n'%len(imagedata_list))
imagedata_list = decrease_sea(imagedata_list)


biome_percents =[]
for i in range(0,len(imagedata_list[0].biomedata)):
  counter = 0
  for j in range(0,len(imagedata_list)):
    counter += imagedata_list[j].biomedata[i]
  biome_percents.append(counter/len(imagedata_list))
  
for i in range(0,len(biome_percents)):
  biome_percents[i]= biome_percents[i]*100
  
print('TSMBForest'+' :  '+'%.2f'%biome_percents[0]+'%')
print('TSDBForest'+' :  '+'%.2f'%biome_percents[1]+'%')
print('TSCForest'+' :  '+'%.2f'%biome_percents[2]+'%')
print('PBMForest'+' :  '+'%.2f'%biome_percents[3]+'%')

print('PCForest'+' :  '+'%.2f'%biome_percents[4]+'%')
print('BForest'+' :  '+'%.2f'%biome_percents[5]+'%')
print('TSGrassland'+' :  '+'%.2f'%biome_percents[6]+'%')
print('PGrassland'+' :  '+'%.2f'%biome_percents[7]+'%')

print('FGrassland'+' :  '+'%.2f'%biome_percents[8]+'%')
print('MGrassland'+' :  '+'%.2f'%biome_percents[9]+'%')
print('Tundra'+' :  '+'%.2f'%biome_percents[10]+'%')
print('DForest'+' :  '+'%.2f'%biome_percents[11]+'%')

print('Desert'+' :  '+'%.2f'%biome_percents[12]+'%')
print('Mangrove'+' :  '+'%.2f'%biome_percents[13]+'%')
print('Lake'+' :  '+'%.2f'%biome_percents[14]+'%')
print('RockIce'+' :  '+'%.2f'%biome_percents[15]+'%')

print('Sea'+' :  '+'%.2f'%biome_percents[16]+'%')

print('\nQuantidade de dados que sobraram: %d'%len(imagedata_list))

print('\n\n')
  
