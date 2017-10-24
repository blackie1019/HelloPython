import shutil,os

targetFile = os.path.join(os.path.dirname(os.getcwd()),'019_MoveFilesAndFolders','test.txt')
shutil.copy(targetFile,  os.path.abspath('copyFile.txt'))

# Create Files

shutil.copy(targetFile,  os.path.abspath('copy\\file1.txt'))
shutil.copy(targetFile,  os.path.abspath('copy\\file2.txt'))

shutil.copytree(os.path.dirname('copy'),os.path.dirname('copy2'))