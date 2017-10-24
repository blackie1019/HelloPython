import shelve

shelveData = shelve.open('myShelveData')
shelveData['players'] = ['MJ','Kobe','LBJ']
shelveData.close()

shelveData = shelve.open('myShelveData')

print(list(shelveData.keys()))

for player in shelveData['players']:    
    print(player)

shelveData['players'] = ['Allen']
print(shelveData['players'] )
shelveData.close()

shelveData = shelve.open('myShelveData')
for player in shelveData['players']:    
    print(player)
shelveData.close()