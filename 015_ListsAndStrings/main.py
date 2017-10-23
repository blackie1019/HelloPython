import copy

name = 'blackie'
print(name[0])

print('bla' in name)

print('blk' in name)

spam = [1,2,3,4,5]
same = spam
spam[0] = 6
print(spam,same)

spamCopy = copy.deepcopy(spam)
spam[0] = 1
print(spam,spamCopy)