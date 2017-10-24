import shelve

fileContent = open(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py')
print(fileContent)
print(fileContent.readline())

for line in fileContent.readlines():
    print(line)

fileContent.close()
fileContent =  open('test.txt','w')
fileContent.write('hello!!')
fileContent.write('I am Blackie')
fileContent.writelines('This is a good day\n')
fileContent.writelines('The End!')
fileContent.close()