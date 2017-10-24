import os

print(os.path.join('folder1','folder2','filename'))

print(os.sep)

print(os.getcwd())
print(os.path.abspath('main.py'))
print(os.path.isabs('main.py'))
print(os.path.isabs(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))
print(os.path.dirname(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))
print(os.path.basename(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))

print(os.path.exists(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))
print(os.path.exists(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main2.py'))

print(os.path.isfile(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))
print(os.path.isfile(r'D:\2.Repo\HelloPython\018_FilesAndFolders'))

print(os.path.isdir(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))
print(os.path.isdir(r'D:\2.Repo\HelloPython\018_FilesAndFolders'))

print(os.path.getsize(r'D:\2.Repo\HelloPython\018_FilesAndFolders\main.py'))

print(os.listdir(r'D:\2.Repo\HelloPython'))

os.chdir('D:\\2.Repo\\HelloPython')
print(os.getcwd())
