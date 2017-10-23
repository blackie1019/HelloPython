print('specail character \",\\,\',\t,\n')

print("""This is content
t
t

t""")

testString = 'abcdEFG'

print('x' in testString)
print('a' in testString)
print('bc' in testString)
print('eF' in testString)
print('FG' in testString)

testString.upper()
print(testString)
print(testString.upper())
print(testString.lower())

print(testString.isupper())
print(testString.islower())
print(testString.lower().islower())

print('abc'.isalpha())
print('abc123'.isalpha())
print('abc123'.isalnum())
print('abc123-'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('Is This a Title'.istitle())
print('Is This A Title'.istitle())

print('abc def'.startswith('a'))
print('abc def'.endswith('f'))
print('abc def'.split(' '))
print('abc'.join(['123','456']))

print('abc'.center(21,'='))
print('abc                   ddd'.strip())
print('   abc                   '.strip())
print('abc'.replace('ab','de'))

name = 'blackie'
place = 'my home'
print('Hello %s, you are invite to the party at %s.' % (name,place))