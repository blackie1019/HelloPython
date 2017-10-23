inputStr = "None"
def doTest():
    inputStr = "Test..."
    print('inside the local:'+inputStr)

def doTest2():
    print('inside the local:'+inputStr)

def doTest3():
    global inputStr
    inputStr = "Global..."
    print('inside the local:'+inputStr)

print(inputStr)
doTest()
print(inputStr)
doTest2()
print(inputStr)
doTest3()
print(inputStr)