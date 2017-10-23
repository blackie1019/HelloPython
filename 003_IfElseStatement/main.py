def doTest():
    print("I am a test function")

def doNothing():
    print("Nothing...")

def testInput(inputValue:bool):
    if(inputValue):
        doTest()
    else:
        doNothing()

print("Please input something")

inputStr = input()

testInput(bool(inputStr))