#! python3
# selectiveCopy.py - walks through a folder tree and searches for files 
# with a certain file extension and copies these files into a new folder.

import os, shutil, sys

# function with 2 arguments: extension, source

def selectiveCopy(extension, source):

# make sure source is absolute
source = os.path.abspath(source)

matchList=[]
	
# walk down file tree of 'source', looking for files ending in 'extension'

for dirpath, dirnames, filenames in os.walk(source):

	for filename in filenames:
		if filename.endswith('.' + extension):
			matchList.append(filename)

# if list length < 0, print none found and end program

if len(matchList) > 0:
	print('No files with specified extension found.')
	sys.exit()

# if list length > 0, create folder with incrementing number if exists

number = 1
while True:	
	folderName = os.path.join(os.path.dirname(source), extension + str(number))
	if not os.path.exists(newFolder):
			break
	number += 1

# create new folder and add files in list

newFolder = os.makedirs(folderName)

print('Files with specified extension copied to %s:' % newFolder)

# copy files in list to new folder and print to screen all files

for filename in matchList:
	shutil.copy(os.path.join(source, filename)), newFolder)
	print(filename)


