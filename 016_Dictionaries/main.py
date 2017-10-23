import pprint

item = {'key1':'123','key2':'hihi',123:'ThisIsNumber'}
print(item['key1'],item[123])

print(item.get('key2','NoThing'))
print(item.get('key4','NoThing'))

item.setdefault('key4','HaveKey4Value')
print(item.get('key4','NoThing'))

item.setdefault('key4','')
print(item.get('key4','NoThing'))

print(item.keys())
print(item.values())

for k,v in item.items():
    print('Key:'+str(k)+',Value:'+str(v))

print(item)
pprint.pprint(item)

items = []
items.append({'key1:':1,'key2:':2,'key3:':3})
items.append({'key1:':10,'key2:':20,'key3:':30})
items.append({'key1:':100,'key2:':200,'key3:':300})
items.append({'key1:':1000,'key2:':2000,'key3:':3000})

print(items)
pprint.pprint(items)