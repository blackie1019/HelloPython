datas = ['1',2,3.0,[1,2,3,4]]
for item in datas:
    print(item)

for item in datas[3]:
    print(item)

print(list('IamAString'))

print(datas[:1])
print(datas[1:])

del datas[3]
print(datas)

print(datas+datas)
print(datas*3)
print('1' in datas)
print('2' in datas)
print('3' not in datas)
print(len(datas))