from typing import Set
import numpy as np
import csv
from numpy import genfromtxt
import io
from PIL import Image
import pandas as pd
from pandas.io.pytables import dropna_doc
from dao import imageDAO
from matplotlib import cm
import json
import base64
from settings import Settings
imageDB = imageDAO(Settings.getDatabase(), Settings.getUser(), Settings.getPassword(), Settings.getHost(), Settings.getPort())

headers = [
    'depth','col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25','col26','col27','col28','col29','col30','col31','col32','col33','col34','col35','col36','col37','col38','col39','col40','col41','col42','col43','col44','col45','col46','col47','col48','col49','col50','col51','col52','col53','col54','col55','col56','col57','col58','col59','col60','col61','col62','col63','col64','col65','col66','col67','col68','col69','col70','col71','col72','col73','col74','col75','col76','col77','col78','col79','col80','col81','col82','col83','col84','col85','col86','col87','col88','col89','col90','col91','col92','col93','col94','col95','col96','col97','col98','col99','col100','col101','col102','col103','col104','col105','col106','col107','col108','col109','col110','col111','col112','col113','col114','col115','col116','col117','col118','col119','col120','col121','col122','col123','col124','col125','col126','col127','col128','col129','col130','col131','col132','col133','col134','col135','col136','col137','col138','col139','col140','col141','col142','col143','col144','col145','col146','col147','col148','col149','col150']

def imageToBytes(imgObj):
    try:
        imgBytes = io.BytesIO()
        imgObj.save(imgBytes, format='png')
        imgBytes = imgBytes.getvalue()
        return imgBytes
    except Exception as e:
        raise e

def bytesToImage(imgBytes):
    try:
        stream = io.BytesIO(imgBytes)
        img = Image.open(stream)
        return img
    except Exception as e:
        raise e

def saveImageDb(imgObj):
    try:
        response = imageDB.insertImage(imageToBytes(imgObj))
    except Exception as e:
        raise e

def resizeImage(fileName):
    try:
        with open(fileName) as csv_file:
            listImg = list(csv.reader(csv_file, delimiter=","))[1:-1] #Skip Headers and Footer
            depth = []
            HEIGHT = len(listImg)
            WIDTH = 150
            for row in listImg:
                depth.append(row.pop(0))
            matrix = np.array(listImg).astype("uint8")  #read csv
            imgObj = Image.fromarray(matrix)  #convert matrix to Image object
            resized_imgObj = imgObj.resize((WIDTH, HEIGHT))  #resize Image object
            resized_imgArray = list(resized_imgObj.getdata()) # convert image data to a list of integers
            # convert that to 2D list (list of lists of integers)
            resized_imgArray = [resized_imgArray[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
            for i in range(len(resized_imgArray)):
                resized_imgArray[i].insert(0, depth[i]) #Putting depth back to the array
            df = pd.DataFrame(np.array(resized_imgArray))
            # df.to_csv('myfile.csv',  header= headers, index=False)
            saveImageDb(resized_imgObj)
        return {'results': 'image resized successfuly', 'success':True}, 200

    except Exception as e:
        raise e


def getFrames(minDepth, maxDepth):
    try:
        imgByte = imageDB.getImage()
        imgObj = bytesToImage(imgByte)
        WIDTH = imgObj.width
        HEIGHT = imgObj.height
        imgArray = list(imgObj.getdata()) # convert image data to a list of integers
        # convert that to 2D list (list of lists of integers)
        imgArray = [imgArray[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]            
        finalImgArray = imgArray[int(minDepth-9000.1)*10:int(maxDepth-9000.1+1)*10]
        df = pd.DataFrame(np.array(finalImgArray))
        
        im = Image.fromarray(np.uint8(cm.gist_earth(finalImgArray)*255))
        # im.save('test2.png')
        img_byte_arr = io.BytesIO()
        im.save(img_byte_arr, format='png')
        img_str = base64.b64encode(img_byte_arr.getvalue())
        return img_str
    except Exception as e:
        raise e

# resizeImage("img[1][1].csv")

def openPlant(fileName):
    return pd.read_excel(fileName, sheet_name= 'PLNT19', skiprows=1)
    
    
def topPlants(n, fileName='egrid2019_data.xlsx'):
    df = openPlant(fileName)
    newDf = df.sort_values('PLNGENAN', ascending=False).head(n)
    return newDf.to_json(double_precision=0, orient="records")


def filterByState(state, fileName='egrid2019_data.xlsx'):
    df = openPlant(fileName)
    newDf = df.loc[df['PSTATABB'] == state]
    return newDf.to_json(double_precision=0, orient="records")

def netGenerationByState(fileName='egrid2019_data.xlsx'):
    df = openPlant(fileName)
    results=[]
    newDf = df.groupby('PSTATABB',dropna=True)[['PLNGENAN']].agg('sum').sort_values('PLNGENAN', ascending=False)
    total = newDf['PLNGENAN'].sum()
    newDf['PERCENTAGE'] = newDf['PLNGENAN'].apply(lambda x: x * 100 / total)
    
    newDf.rename(columns={'PLNGENAN': 'ABSOLUTE'}, inplace=True)

    return newDf.to_json(double_precision=1)
