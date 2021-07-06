# The default path for scanning, saving csv is the root folder where you are running this script.
# The default name of csv is result.csv
# If you want to overwrite the default path to scan path to save csv, csv name then run the script in following manner:
# python3 main_csv.py /your_path_to_scan /your_path_to_save filename.csv
# Eg: python3 main_csv.py /home/daksh/Desktop/cdli_test_images /home/daksh/Desktop data.csv
# This will prompt the script to scan the folder in the given path, save the csv in next path, name the csv accordingly.

# Running the Script:
# 1) Create the virtual environment:
# python3 -m venv env
# 
# 2) Activate the environement:
# source env/bin/activate
#
# 3) Install requirements:
# pip3 install -r requirements.txt
#
# 4) Run the script:
# python3 main_csv.py

import os
import datetime
import sys
import pandas as pd
import cv2
from PIL import Image
import colorama
from colorama import Fore

# Function to get the directories name, file path, root
def get_filepaths(directory):
    file_paths = []
    file_extension = []
    root_path = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(filename)
            root_path.append(root)
            filextension = os.path.splitext(filepath)[1]
            file_paths.append(filepath) 
            file_extension.append(filextension)
    #print(file_paths)
    #print(file_extension)
    #print(root_path)
    return file_paths, file_extension, root_path

# Calling function for different folders
n=len(sys.argv)
if(n==1):
    directory=os.path.dirname(os.path.abspath(__file__))
    directory_json=os.path.dirname(os.path.abspath(__file__))
    file_csv_name="result.csv"

elif(n==2):
    directory=sys.argv[1]
    directory_json=os.path.dirname(os.path.abspath(__file__))
    file_csv_name="result.csv"

elif(n==3):
    directory=sys.argv[1]
    directory_json=sys.argv[2]
    file_csv_name="result.csv"
    
else:
    directory=sys.argv[1]
    directory_json=sys.argv[2]
    file_csv_name=sys.argv[3]
#eps = get_filepaths(directory+"/eps")
lineart = get_filepaths(directory+"/lineart")
long_translit = get_filepaths(directory+"/long_translit")
pdf = get_filepaths(directory+"/pdf")
photo = get_filepaths(directory+"/photo")
ptm = get_filepaths(directory+"/ptm")
svg = get_filepaths(directory+"/svg")
tn_lineart = get_filepaths(directory+"/tn_lineart")
tn_photo = get_filepaths(directory+"/tn_photo")
vcmodels = get_filepaths(directory+"/vcmodels")
mode_to_bpp = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}

print("Fetching File Names....")
#Storing the data and dumping it in .json file
file_name=[]
#for i in range(len(eps[0])):
    #item=eps[0][i]
    #file_name.append(item)

for i in range(len(lineart[0])):
    item=lineart[0][i]
    file_name.append(item)

for i in range(len(long_translit[0])):
    item=long_translit[0][i]
    file_name.append(item)

for i in range(len(pdf[0])):
    item=pdf[0][i]
    file_name.append(item)

for i in range(len(photo[0])):
    item=photo[0][i]
    file_name.append(item)

for i in range(len(ptm[0])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        item=ptm[0][i]
        file_name.append(item)

for i in range(len(svg[0])):
    item=svg[0][i]
    file_name.append(item)

for i in range(len(tn_lineart[0])):
    item=tn_lineart[0][i]
    file_name.append(item)

for i in range(len(tn_photo[0])):
    item=tn_photo[0][i]
    file_name.append(item)

for i in range(len(vcmodels[0])):
    item=vcmodels[0][i]
    file_name.append(item)

print("Fetching File names...."+Fore.GREEN+"done \n")

print(Fore.WHITE+"Fetching Folder name....")
folder_name=[]
#for i in range(len(eps[2])):
    #item=eps[2][i][len(directory):]
    #folder_name.append(item)

for i in range(len(lineart[2])):
    item=lineart[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(long_translit[2])):
    item=long_translit[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(pdf[2])):
    item=pdf[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(photo[2])):
    item=photo[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(ptm[2])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        item=ptm[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(svg[2])):
    item=svg[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(tn_lineart[2])):
    item=tn_lineart[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(tn_photo[2])):
    item=tn_photo[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(vcmodels[2])):
    item=vcmodels[2][i][len(directory):]
    folder_name.append(item)

print("Fecthing Folder Name...."+Fore.GREEN+"done \n")
artifact_id=[]
print(Fore.WHITE+"Fecthing Artifact ID....")

#for i in range(len(eps[0])):
    #item=eps[0][i][1:-4]
    #artifact_id.append(item)

for i in range(len(lineart[0])):
    item=lineart[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(long_translit[0])):
    item=long_translit[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(pdf[0])):
    item=pdf[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(photo[0])):
    item=photo[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(ptm[0])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        item=ptm[2][i][len(directory)+6: -2]
        artifact_id.append(item.strip("0"))

for i in range(len(svg[0])):
    item=svg[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(tn_lineart[0])):
    item=tn_lineart[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(tn_photo[0])):
    item=tn_photo[0][i][1:7]
    artifact_id.append(item.strip("0"))

for i in range(len(vcmodels[0])):
    item=vcmodels[2][i][len(directory)+11:]
    artifact_id.append(item.strip("0"))

print("Fecthing Artifact ID...."+Fore.GREEN+"done \n")
image_type=[]
print(Fore.WHITE+"Fecthing Image Type....")

#for i in range(len(eps[0])):
    #item="eps"
    #image_type.append(item)

for i in range(len(lineart[0])):
    if(lineart[0][i][8:10]=="ld"):
        item="lineart_detail"
    else:
        item="lineart"
    image_type.append(item)

for i in range(len(long_translit[0])):
    item="long translit"
    image_type.append(item)

for i in range(len(pdf[0])):
    item="pdf"
    image_type.append(item)

for i in range(len(photo[0])):
    if(photo[0][i][8:9]=="d"):
        item="photo_detail"
    elif(photo[0][i][8:9]=="e"):
        item="photo_enevelope"
    else:
        item="photo"
    image_type.append(item)

for i in range(len(ptm[0])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        item="ptm"
        image_type.append(item)

for i in range(len(svg[0])):
    item="svg"
    image_type.append(item)

for i in range(len(tn_lineart[0])):
    item="thumb lineart"
    image_type.append(item)

for i in range(len(tn_photo[0])):
    item="thumb photo"
    image_type.append(item)

for i in range(len(vcmodels[0])):
    item="3D models"
    image_type.append(item)

print("Fetching Image Type...."+Fore.GREEN+"done \n")
height=[]
width=[]
rgb=[]
bit=[]
ppi=[]
size_bytes=[]
pixels=[]
print(Fore.WHITE+"Fetching Height, Width, Size, PPI, Bits....")
#for i in range(len(eps[0])):
    #item=eps[0][i]
    #file_name.append(item)

for i in range(len(lineart[0])):
    item=lineart[0][i]
    im=cv2.imread(lineart[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(lineart[2][i]+"/"+item)
    colors=image.getpixel((320,240))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(lineart[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)

for i in range(len(long_translit[0])):
    item=long_translit[0][i]
    im=cv2.imread(long_translit[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(long_translit[2][i]+"/"+item)
    colors=image.getpixel((320,420))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(long_translit[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)

for i in range(len(pdf[0])):
    item=pdf[0][i]
    height.append("")
    width.append("")
    rgb.append("")
    bit.append("")
    ppi.append("")
    size_bytes.append("")
    pixels.append("")

for i in range(len(photo[0])):
    item=photo[0][i]
    im=cv2.imread(photo[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(photo[2][i]+"/"+item)
    colors=image.getpixel((320,420))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(photo[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)

for i in range(len(ptm[0])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        item=ptm[0][i]
        im=cv2.imread(ptm[2][i]+"/"+item)
        h,w,c=im.shape
        height.append(h)
        width.append(w)
        image=Image.open(ptm[2][i]+"/"+item)
        colors=image.getpixel((320,420))
        rgb.append(colors)
        bpp = mode_to_bpp[image.mode]
        bit.append(bpp)
        ppi_value=w/(w*0.01)
        ppi.append(ppi_value)
        size_value=str((os.stat(ptm[2][i]+"/"+item).st_size)*0.000001)
        size_bytes.append(size_value)
        pixels_value=w*h
        pixels.append(pixels_value)

for i in range(len(svg[0])):
    item=svg[0][i]
    height.append("")
    width.append("")
    rgb.append("")
    bit.append("")
    ppi.append("")
    size_bytes.append("")
    pixels.append("")

for i in range(len(tn_lineart[0])):
    item=tn_lineart[0][i]
    im=cv2.imread(tn_lineart[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(tn_lineart[2][i]+"/"+item)
    colors=image.getpixel((320,420))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(tn_lineart[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)

for i in range(len(tn_photo[0])):
    item=tn_photo[0][i]
    im=cv2.imread(tn_photo[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(tn_photo[2][i]+"/"+item)
    colors=image.getpixel((320,420))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(tn_photo[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)

for i in range(len(vcmodels[0])):
    item=vcmodels[0][i]
    height.append("")
    width.append("")
    rgb.append("")
    bit.append("")
    ppi.append("")
    size_bytes.append("")
    pixels.append("")

print("Fetching Height, Width, Size, PPI, Bits...."+Fore.GREEN+"done \n")
modified_date=[]
created_date=[]
print(Fore.WHITE+"Fecthing Dates....")
#for i in range(len(eps[0])):
    #create=time.ctime(os.path.getctime(eps[2][i]+"/"+eps[0][i]))
    #modify=time.ctime(os.path.getmtime(eps[2][i]+"/"+eps[0][i]))
    #created_date.append(create)
    #modified_date.append(modify)

for i in range(len(lineart[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(lineart[2][i]+"/"+lineart[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(lineart[2][i]+"/"+lineart[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(long_translit[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(long_translit[2][i]+"/"+long_translit[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(long_translit[2][i]+"/"+long_translit[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(pdf[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(pdf[2][i]+"/"+pdf[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(pdf[2][i]+"/"+pdf[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(photo[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(photo[2][i]+"/"+photo[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(photo[2][i]+"/"+photo[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(ptm[0])):
    if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(ptm[2][i]+"/"+ptm[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(ptm[2][i]+"/"+ptm[0][i]))
        created_date.append(create)
        modified_date.append(modify)

for i in range(len(svg[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(svg[2][i]+"/"+svg[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(svg[2][i]+"/"+svg[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(tn_lineart[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(tn_lineart[2][i]+"/"+tn_lineart[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(tn_lineart[2][i]+"/"+tn_lineart[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(tn_photo[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(tn_photo[2][i]+"/"+tn_photo[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(tn_photo[2][i]+"/"+tn_photo[0][i]))
    created_date.append(create)
    modified_date.append(modify)

for i in range(len(vcmodels[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(vcmodels[2][i]+"/"+vcmodels[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(vcmodels[2][i]+"/"+vcmodels[0][i]))
    created_date.append(create)
    modified_date.append(modify)

print("Fetching Dates...."+Fore.GREEN+"done \n")
dict={"file_name":file_name, "folder_name":folder_name, "artifact_id":artifact_id, "image_type": image_type, "creation_date":created_date, "modify_date":modified_date, "height":height, "width":width, "rgb":rgb, "bit":bit, "ppi":ppi, "size_mb":size_bytes, "size_pixels":pixels}
dataframe=pd.DataFrame(dict)
dataframe.to_csv(directory_json+"/"+file_csv_name, index=False)
print(Fore.WHITE+"Successfully Dumped at "+Fore.GREEN+directory_json+"/"+file_csv_name)