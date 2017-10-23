def hello(inputStr):
    output = 'Hello,' + inputStr + '!'
    age = '32'
    text = 'hahah ' + str(int(age)+1.5)
    print(output+text)

print('Please input your name!') #Test Comment
myName = input()
hello(myName)
print('Your name length = '+str(len(myName)))