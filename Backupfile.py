import os
import shutil
import dropbox

source=input("Enter the Source folder name :")
destination=input("Enter the Destination folder name :")
source = source + '/'
destination = destination + '/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source + file),destination)