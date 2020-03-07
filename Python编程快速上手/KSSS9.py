#复制文件
import shutil,os
paper = open('c:\\users\\MI\\test.txt','w')
os.chdir('c:\\')
shutil.copy('c:\\users\\MI\\test.txt','d:\\')
shutil.copytree('C:\\Users\\Public','d:\\Users')
#文件和文件夹的移动和改名
import shutil,os
shutil.move('d:\\test.txt','d:\\users')
shutil.move('d:\\users\\test.txt','c:\\users\\MI\\new_test.txt')
#永久删除文件和文件夹
import os
for filename in os.listdir():
    if filename.endswith('.txt')
        os.unlink()
#删除的函数包括：os.unlink(path),os.rmdir(path),os.rmtree(path)

# 用send2trash模块安全地删除
import send2trash
baconFile = open('c:\\users\\MI\\new_test.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('c:\\users\\MI\\new_test.txt')

#遍历目录树
import os
for folderName, subfolders, filenames in os.walk('c:\\users\\MI'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)
    print('')

# 用zipfile模块压缩文件
import zipfile, os
os.chdir('d:\\users') #move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
pigInfo = exampleZip.getinfo('pig.txt')
pigInfo.file_size
pigInfo.compress_size
'Compressed file is %sx smaller!' % (round(pigInfo.file_size / pigInfo.compress_size, 2))
exampleZip.close()

# 用zipfile模块解压文件
import zipfile, os
os.chdir('d:\\users')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('pig.txt') #解压单个文件
exampleZip.extract('pig.txt','c:\\users\\MI') #解压文件到指定的途径
exampleZip.close()

# 创建和添加到ZIP文件
import zipfile
newZip = zipfile.ZipFile('d:\\users\\new.zip','w')
newZip.write('pigwang.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# 项目：将带有美国风格日期的文件改名为欧洲风格日期
import shutil, os, re

#create a regex that matches files with the American date format.
datePattern = re.compile(r'''(.*?)  # all text before the date.
              ((0|1)?\d)- # one or two digits for the month
              ((0|1|2|3)?\d)- # one or two digits for the day
              ((19|20)\d\d) # four digits for the year
              (.*?)$ # all text after the date
              ''',re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
# Skip files without a date.
    if mo == None:
        continue
# Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
# Form the European - style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + '-' + afterPart
# Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)
# Rename the files.
    print('Renameing "%s" to "%s"...' % (amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)

# 项目：将一个文件夹备份到ZIP文件
import zipfile, os
def backupTozip(folder):
    # Backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute.

    # Figure out the filename this code should use based on
    # What files already exist.
    number = 1
    while True:
        zipFilname = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilname):
            break
        number = number + 1

    # Create the ZIP file.
    print('Create %s...' % (zipFilname))
    backupZip  = zipfile.ZipFile(zipFilname,'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #Add the current folder to the ZIP file.
        backupZip.write(foldername)
    # Add all the files ini this folder to the ZIP file.
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue # Don't backup ZIP files
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupTozip('c:\\delicious')
