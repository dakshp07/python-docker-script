# Author: Daksh Paleria
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
import shutil
import numpy as np
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

# Creating directories for 3D Models
for file in os.scandir(directory+"/vcmodels"):
    if(file.name[0]=="P"):
        if(file.name[8:9]=="e"):
            path_vcmodel_one_arti=os.path.join(directory+"/vcmodels", file.name[0:7]+"_"+file.name[8:9])
            os.makedirs(path_vcmodel_one_arti, exist_ok=True)
            if(file.name[0:9]==path_vcmodel_one_arti[-9:]):
                shutil.move(directory+"/vcmodels/"+file.name,path_vcmodel_one_arti)
        else:
            path_vcmodel_one_arti=os.path.join(directory+"/vcmodels", file.name[0:7])
            os.makedirs(path_vcmodel_one_arti, exist_ok=True)
            if(file.name[0:7]==path_vcmodel_one_arti[-7:]):
                shutil.move(directory+"/vcmodels/"+file.name,path_vcmodel_one_arti)

#eps = get_filepaths(directory+"/eps")
lineart = get_filepaths(directory+"/lineart")
long_translit = get_filepaths(directory+"/long_translit")
pdf = get_filepaths(directory+"/pdf")
photo = get_filepaths(directory+"/photo")
ptm = get_filepaths(directory+"/ptm")
svg = get_filepaths(directory+"/svg")
vcmodels = get_filepaths(directory+"/vcmodels")
rti=get_filepaths(directory+"/rti")
mode_to_bpp = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}


#Storing the data and dumping it in .json file
file_name=[]
file_name_vc=[]
#for i in range(len(eps[0])):
    #item=eps[0][i]
    #file_name.append(item)

for i in range(len(lineart[0])):
    if (lineart[0][i][0]=="P"):
        item=lineart[0][i]
        file_name.append(item)

for i in range(len(long_translit[0])):
    if (long_translit[0][i][0]=="P"):
        item=long_translit[0][i]
        file_name.append(item)

for i in range(len(pdf[0])):
    if (pdf[0][i][0]=="P"):
        item=pdf[0][i]
        file_name.append(item)

for i in range(len(photo[0])):
    if (photo[0][i][0]=="P"):
        item=photo[0][i]
        file_name.append(item)

for i in range(len(ptm[0])):
    if (ptm[0][i][0]=="P"):
        if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
            item=ptm[0][i]
            file_name.append(item)

for i in range(len(svg[0])):
    if (svg[0][i][0]=="P"):
        item=svg[0][i]
        file_name.append(item)

for i in range(len(vcmodels[0])):
    if (vcmodels[0][i][0]=="P"):
        item=vcmodels[0][i]
        file_name_vc.append(item)
        file_name_vc_split=np.array_split(file_name_vc,(len(vcmodels[0])/2))

for i in range(len(rti[0])):
    item=rti[0][i]
    file_name.append(item)

for i in range(len(vcmodels[0])//2):
    if(file_name_vc_split[i][0][-3:]=="jpg"):
        file_name.append(file_name_vc_split[i][0])
    elif (file_name_vc_split[i][1][-3:]=="jpg"):
        file_name.append(file_name_vc_split[i][1])

folder_name=[]
folder_name_vc=[]
#for i in range(len(eps[2])):
    #item=eps[2][i][len(directory):]
    #folder_name.append(item)

for i in range(len(lineart[2])):
    if (lineart[0][i][0]=="P"):
        item=lineart[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(long_translit[2])):
    if (long_translit[0][i][0]=="P"):
        item=long_translit[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(pdf[2])):
    if (pdf[0][i][0]=="P"):
        item=pdf[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(photo[2])):
    if (photo[0][i][0]=="P"):
        item=photo[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(ptm[2])):
    if (ptm[0][i][0]=="P"):
        if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
            item=ptm[2][i][len(directory):]
            folder_name.append(item)

for i in range(len(svg[2])):
    if (svg[0][i][0]=="P"):
        item=svg[2][i][len(directory):]
        folder_name.append(item)

for i in range(len(vcmodels[2])):
    if (vcmodels[0][i][0]=="P"):
        item=vcmodels[2][i][len(directory):]
        folder_name_vc.append(item)
        folder_name_vc_split=np.array_split(folder_name_vc, (len(vcmodels[0])/2))

for i in range(len(rti[2])):
    item=rti[2][i][len(directory):]
    folder_name.append(item)

for i in range(len(vcmodels[2])//2):
    if(file_name_vc_split[i][0][-3:]=="jpg"):
        folder_name.append(folder_name_vc_split[i][0])
    elif (file_name_vc_split[i][1][-3:]=="jpg"):
        folder_name.append(folder_name_vc_split[i][1])


artifact_id=[]
artifact_id_vc=[]
print(Fore.WHITE+"Fecthing Artifact ID....")

#for i in range(len(eps[0])):
    #item=eps[0][i][1:-4]
    #artifact_id.append(item)

for i in range(len(lineart[0])):
    if (lineart[0][i][0]=="P"):
        item=lineart[0][i][1:7]
        artifact_id.append(item.strip("0"))

for i in range(len(long_translit[0])):
    if (long_translit[0][i][0]=="P"):
        item=long_translit[0][i][1:7]
        artifact_id.append(item.strip("0"))

for i in range(len(pdf[0])):
    if (pdf[0][i][0]=="P"):
        item=pdf[0][i][1:7]
        artifact_id.append(item.strip("0"))

for i in range(len(photo[0])):
    if (photo[0][i][0]=="P"):
        item=photo[0][i][1:7]
        artifact_id.append(item.strip("0"))

for i in range(len(ptm[0])):
    if (ptm[0][i][0]=="P"):
        if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
            item=ptm[2][i][len(directory)+6: -2]
            artifact_id.append(item.strip("0"))

for i in range(len(svg[0])):
    if (svg[0][i][0]=="P"):
        item=svg[0][i][1:7]
        artifact_id.append(item.strip("0"))


for i in range(len(vcmodels[0])):
    if (vcmodels[0][i][0]=="P"):
        item=vcmodels[2][i][len(directory)+11:]
        if((vcmodels[2][i][len(directory)+11:])[-1:]=="e" or (vcmodels[2][i][len(directory)+11:])[-1:]=="a" or (vcmodels[2][i][len(directory)+11:])[-1:]=="b"):
            artifact_id_vc.append(item[0:6].strip("0"))
            artifact_id_vc_split=np.array_split(artifact_id_vc,(len(vcmodels[0])/2))
        else:
            artifact_id_vc.append(item.strip("0"))
            artifact_id_vc_split=np.array_split(artifact_id_vc,(len(vcmodels[0])/2))

for i in range(len(rti[0])):
    if(rti[2][i][-1]=="o" or rti[2][i][-1]=="r"):
        item=rti[2][i][len(directory)+6:-2]
        artifact_id.append(item.strip("0"))
    else:
        item=rti[2][i][len(directory)+6:-3]
        artifact_id.append(item.strip("0"))

for i in range(len(vcmodels[0])//2):
    if(file_name_vc_split[i][0][-3:]=="jpg"):
        artifact_id.append(artifact_id_vc_split[i][0])
    elif (file_name_vc_split[i][1][-3:]=="jpg"):
        artifact_id.append(artifact_id_vc_split[i][1])

print("Fecthing Artifact ID...."+Fore.GREEN+"done \n")
image_type=[]
image_subtype=[]
image_subtype_vc=[]
image_type_vc=[]
print(Fore.WHITE+"Fecthing Image Type and Subtype....")

#for i in range(len(eps[0])):
    #item="eps"
    #image_type.append(item)

for i in range(len(lineart[0])):
    if (lineart[0][i][0]=="P"):
        if(lineart[0][i][8:10]=="ld"):
            item="lineart"
            item_1="detail"
        elif(lineart[0][i][8:10]=="ls"):
            item="lineart"
            item_1="seal"
        else:
            item="lineart"
            item_1=""
        image_type.append(item)
        image_subtype.append(item_1)

for i in range(len(long_translit[0])):
    if (long_translit[0][i][0]=="P"):
        item="long"
        item_1="translit"
        image_type.append(item)
        image_subtype.append(item_1)

for i in range(len(pdf[0])):
    if (pdf[0][i][0]=="P"):
        item="pdf"
        item_1=""
        image_subtype.append(item_1)
        image_type.append(item)

for i in range(len(photo[0])):
    if (photo[0][i][0]=="P"):
        if(photo[0][i][8:9]=="d"):
            item="photo"
            item_1="detail"
        elif(photo[0][i][8:9]=="s"):
            item="photo"
            item_1="seal"
        elif(photo[0][i][8:9]=="e"):
            item="photo"
            item_1="envelope"
        else:
            item="photo"
            item_1=""
        image_subtype.append(item_1)
        image_type.append(item)

for i in range(len(ptm[0])):
    if (ptm[0][i][0]=="P"):
        if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
            item="ptm"
            item_1=""
            image_subtype.append(item_1)
            image_type.append(item)

for i in range(len(svg[0])):
    if (svg[0][i][0]=="P"):
        item="svg"
        item_1=""
        image_subtype.append(item_1)
        image_type.append(item)

for i in range(len(vcmodels[0])):
    if (vcmodels[0][i][0]=="P"):
        if (vcmodels[2][i][-1]=="e"):
            item="3D_model"
            item_1="e"
            image_subtype_vc.append(item_1)
            image_type_vc.append(item)
            image_type_vc_split=np.array_split(image_type_vc,(len(vcmodels[0])/2))
            image_subtype_vc_split=np.array_split(image_subtype_vc,(len(vcmodels[0])/2))
        elif (vcmodels[2][i][-1]=="a"):
            item="3D_model"
            item_1="a"
            image_subtype_vc.append(item_1)
            image_type_vc.append(item)
            image_type_vc_split=np.array_split(image_type_vc,(len(vcmodels[0])/2))
            image_subtype_vc_split=np.array_split(image_subtype_vc,(len(vcmodels[0])/2))
        elif (vcmodels[2][i][-1]=="b"):
            item="3D_model"
            item_1="b"
            image_subtype_vc.append(item_1)
            image_type_vc.append(item)
            image_type_vc_split=np.array_split(image_type_vc,(len(vcmodels[0])/2))
            image_subtype_vc_split=np.array_split(image_subtype_vc,(len(vcmodels[0])/2))
        else:
            item="3D_model"
            item_1=""
            image_subtype_vc.append(item_1)
            image_type_vc.append(item)
            image_type_vc_split=np.array_split(image_type_vc,(len(vcmodels[0])/2))
            image_subtype_vc_split=np.array_split(image_subtype_vc,(len(vcmodels[0])/2))

for i in range(len(rti[0])):
    if(rti[2][i][-1]=="o"):
        item="rti"
        item_1="observe"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-2]=='l'):
        item="rti"
        item_1="left_edge"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-2]=='b'):
        item="rti"
        item_1="bottom_edge"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-1]=='r'):
        item="rti"
        item_1="reverse"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-2]=='t'):
        item="rti"
        item_1="top_edge"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-2]=='r'):
        item="rti"
        item_1="right_edge"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-1]=='a'):
        item="rti"
        item_1="face_a"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-1]=='b'):
        item="rti"
        item_1="face_b"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-1]=='c'):
        item="rti"
        item_1="face_c"
        image_subtype.append(item_1)
        image_type.append(item)
    elif(rti[2][i][-1]=='d'):
        item="rti"
        item_1="face_d"
        image_subtype.append(item_1)
        image_type.append(item)
##print(rti[2][i][-2])
    
for i in range(len(vcmodels[0])//2):
    if(file_name_vc_split[i][0][-3:]=="jpg"):
        image_type.append(image_type_vc_split[i][0])
        image_subtype.append(image_subtype_vc_split[i][0])
    elif (file_name_vc_split[i][1][-3:]=="jpg"):
        image_type.append(image_type_vc_split[i][1])
        image_subtype.append(image_subtype_vc_split[i][1])

print("Fetching Image Type and Subtype...."+Fore.GREEN+"done \n")
height=[]
height_vc=[]
width=[]
width_vc=[]
rgb=[]
rgb_vc=[]
bit=[]
bits_vc=[]
ppi=[]
ppi_vc=[]
size_bytes=[]
size_bytes_vc=[]
pixels=[]
pixels_vc=[]
format=[]
format_vc=[]
print(Fore.WHITE+"Fetching Height, Width, Size, PPI, Bits....")
#for i in range(len(eps[0])):
    #item=eps[0][i]
    #file_name.append(item)

for i in range(len(lineart[0])):
    if (lineart[0][i][0]=="P"):
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
        format.append(lineart[1][i])

for i in range(len(long_translit[0])):
    if (long_translit[0][i][0]=="P"):
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
        format.append(long_translit[1][i])

for i in range(len(pdf[0])):
    if (pdf[0][i][0]=="P"):
        item=pdf[0][i]
        height.append("")
        width.append("")
        rgb.append("")
        bit.append("")
        ppi.append("")
        size_bytes.append("")
        pixels.append("")
        format.append(pdf[1][i])

for i in range(len(photo[0])):
    if (photo[0][i][0]=="P"):
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
        format.append(photo[1][i])

for i in range(len(ptm[0])):
    if (ptm[0][i][0]=="P"):
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
            format.append(ptm[1][i])

for i in range(len(svg[0])):
    if (svg[0][i][0]=="P"):
        item=svg[0][i]
        height.append("")
        width.append("")
        rgb.append("")
        bit.append("")
        ppi.append("")
        size_bytes.append("")
        pixels.append("")
        format.append(svg[1][i])

for i in range(len(vcmodels[0])):
    if (vcmodels[0][i][0]=="P"):
        if(vcmodels[0][i][-3:]=="jpg"):
            item=vcmodels[0][i]
            im=cv2.imread(vcmodels[2][i]+"/"+item)
            h,w,c=im.shape
            height_vc.append(h)
            height_vc_split=np.array_split(height_vc,(len(vcmodels[0])/2))
            width_vc.append(w)
            width_vc_split=np.array_split(width_vc,(len(vcmodels[0])/2))
            image=Image.open(vcmodels[2][i]+"/"+item)
            colors=image.getpixel((320,420))
            rgb_vc.append(colors)
            rgb_vc_split=np.array_split(rgb_vc,(len(vcmodels[0])/2))
            bpp = mode_to_bpp[image.mode]
            bits_vc.append(bpp)
            bits_vc_split=np.array_split(bits_vc,(len(vcmodels[0])/2))
            ppi_value=w/(w*0.01)
            ppi_vc.append(ppi_value)
            ppi_vc_split=np.array_split(ppi_vc,(len(vcmodels[0])/2))
            size_value=str((os.stat(vcmodels[2][i]+"/"+item).st_size)*0.000001)
            size_bytes_vc.append(size_value)
            size_bytes_vc_split=np.array_split(size_bytes_vc,(len(vcmodels[0])/2))
            pixels_value=w*h
            pixels_vc.append(pixels_value)
            pixels_vc_split=np.array_split(pixels_vc,(len(vcmodels[0])/2))
            format_vc.append(vcmodels[1][i])
            format_vc_split=np.array_split(format_vc,(len(vcmodels[0])/2))
        

for i in range(len(rti[0])):
    item=rti[0][i]
    im=cv2.imread(rti[2][i]+"/"+item)
    h,w,c=im.shape
    height.append(h)
    width.append(w)
    image=Image.open(rti[2][i]+"/"+item)
    colors=image.getpixel((320,420))
    rgb.append(colors)
    bpp = mode_to_bpp[image.mode]
    bit.append(bpp)
    ppi_value=w/(w*0.01)
    ppi.append(ppi_value)
    size_value=str((os.stat(rti[2][i]+"/"+item).st_size)*0.000001)
    size_bytes.append(size_value)
    pixels_value=w*h
    pixels.append(pixels_value)
    format.append(rti[1][i])
    
for i in range(len(vcmodels[0])//2): 
    
    format.append(format_vc_split[i][0])
    height.append(height_vc_split[i][0])
    width.append(width_vc_split[i][0])
    rgb.append(rgb_vc_split[i][0])
    ppi.append(ppi_vc_split[i][0])
    size_bytes.append(size_bytes_vc_split[i][0])
    pixels.append(pixels_vc_split[i][0])
    bit.append(bits_vc_split[i][0])

print("Fetching Height, Width, Size, PPI, Bits...."+Fore.GREEN+"done \n")
modified_date=[]
created_date=[]
modified_date_vc=[]
created_date_vc=[]
print(Fore.WHITE+"Fecthing Dates....")
#for i in range(len(eps[0])):
    #create=time.ctime(os.path.getctime(eps[2][i]+"/"+eps[0][i]))
    #modify=time.ctime(os.path.getmtime(eps[2][i]+"/"+eps[0][i]))
    #created_date.append(create)
    #modified_date.append(modify)

for i in range(len(lineart[0])):
    if (lineart[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(lineart[2][i]+"/"+lineart[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(lineart[2][i]+"/"+lineart[0][i]))
        created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
        modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(long_translit[0])):
    if (long_translit[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(long_translit[2][i]+"/"+long_translit[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(long_translit[2][i]+"/"+long_translit[0][i]))
        created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
        modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(pdf[0])):
    if (pdf[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(pdf[2][i]+"/"+pdf[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(pdf[2][i]+"/"+pdf[0][i]))
        created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
        modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(photo[0])):
    if (photo[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(photo[2][i]+"/"+photo[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(photo[2][i]+"/"+photo[0][i]))
        created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
        modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(ptm[0])):
    if (ptm[0][i][0]=="P"):
        if(ptm[2][i][-1]=="o" or ptm[2][i][-1]=="r"):
            create=datetime.datetime.fromtimestamp(os.path.getctime(ptm[2][i]+"/"+ptm[0][i]))
            modify=datetime.datetime.fromtimestamp(os.path.getmtime(ptm[2][i]+"/"+ptm[0][i]))
            created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
            modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(svg[0])):
    if (svg[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(svg[2][i]+"/"+svg[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(svg[2][i]+"/"+svg[0][i]))
        created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
        modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))

for i in range(len(vcmodels[0])):
    if (vcmodels[0][i][0]=="P"):
        create=datetime.datetime.fromtimestamp(os.path.getctime(vcmodels[2][i]+"/"+vcmodels[0][i]))
        modify=datetime.datetime.fromtimestamp(os.path.getmtime(vcmodels[2][i]+"/"+vcmodels[0][i]))
        create_date=create.strftime('%Y-%m-%d %H:%M:%S')
        modify_date=modify.strftime('%Y-%m-%d %H:%M:%S')
        created_date_vc.append(create_date)
        created_date_vc_split=np.array_split(created_date_vc,(len(vcmodels[0])/2))
        modified_date_vc.append(modify_date)
        modified_date_vc_split=np.array_split(modified_date_vc,(len(vcmodels[0])/2))

for i in range(len(rti[0])):
    create=datetime.datetime.fromtimestamp(os.path.getctime(rti[2][i]+"/"+rti[0][i]))
    modify=datetime.datetime.fromtimestamp(os.path.getmtime(rti[2][i]+"/"+rti[0][i]))
    created_date.append(create.strftime("%Y-%m-%d, %H:%M:%S"))
    modified_date.append(modify.strftime("%Y-%m-%d, %H:%M:%S"))
    
for i in range(len(vcmodels[0])//2):
    if(file_name_vc_split[i][0][-3:]=="jpg"):
        created_date.append(created_date_vc_split[i][0])
        modified_date.append(modified_date_vc_split[i][0])
    elif (file_name_vc_split[i][1][-3:]=="jpg"):
        modified_date.append(modified_date_vc_split[i][1])
        created_date.append(created_date_vc_split[i][1])
    #created_date.append(created_date_vc_split[i])
    #modified_date.append(modified_date_vc_split[i])

#print(len(file_name))
#print(len(folder_name))
#print(len(artifact_id))
#print(len(image_type))
#print(len(created_date))
#print(len(modified_date))
#print(len(height))
#print(len(width))
#print(len(rgb))
#print(len(size_bytes))
#print(len(pixels))
print("Fetching Dates...."+Fore.GREEN+"done \n")
dict={"artifact_id":artifact_id, "subtype": image_subtype, "image_type": image_type, "created":created_date, "modified":modified_date, "height":height, "width":width, "rgb":rgb, "bit":bit, "ppi":ppi, "size_mb":size_bytes, "size_pixels":pixels, "format":format}
##print(dict)
dataframe=pd.DataFrame(dict)
dataframe.to_csv(directory_json+"/"+file_csv_name, index=False)
print(Fore.WHITE+"Successfully Dumped at "+Fore.GREEN+directory_json+"/"+file_csv_name)
