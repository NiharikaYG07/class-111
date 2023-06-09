import os
import shutil

destination="C:/Users/aggar/OneDrive/Desktop/python projects/class 110/document_files"
source="C:/Users/aggar/Downloads/coding niharika"
list=os.listdir(source)
print(list)

for i in list:
    root,ext=os.path.splitext(i)
    print(root,ext)


