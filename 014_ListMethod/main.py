spam = ['hello','hi','yo','good morning']

print(spam.index('yo'))

print(len(spam))
spam.append('Yo')
print(len(spam))

spam.insert(1,'good night')
print(spam)

spam.remove('good morning')
print(spam)

spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam.sort(key=str.lower)
print(spam)