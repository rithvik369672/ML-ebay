import pandas as pd
import re

data=pd.read_csv(r'C:\Users\HSU\Desktop\ML ebay\mlchallenge_set_2021.tsv\mlchallenge_set_2021.tsv',encoding = "ISO-8859-1", sep='\t',header=None )

data.columns=["Category","primary_image_url","all_image_url","attribute","index"]



n=1000 #enter the number of data that want to extract

#add empty column
data["Brand"]=""
data["US Shoe Size"]=""
data["Style"]=""
data["Material"]=""
data["Country/Region of Manufacture"]=""
data["Width"]=""

def entrydata(data,column,i):    #column is the colname datatype:string;
    try:
        a=re.search(column,data["attribute"][i]).span()
        temp=data["attribute"][i][a[1]+1:]
        a=re.search(',',temp).span()
        data[column][i]=temp[0:a[0]]
    except AttributeError:
        data[column][i]="N\A"


def entrydatashoesize(data,column,i):    #column is the colname datatype:string;
    try:
        a=re.search(column,data["attribute"][i]).span()
        temp=data["attribute"][i][a[1]+9:]
        a=re.search(',',temp).span()
        data[column][i]=temp[0:a[0]]
    except AttributeError:
        data[column][i]="N\A"

    


for i in range(0,n):
    data["attribute"][i] =data["attribute"][i][1:]
    data["attribute"][i] =data["attribute"][i][0:len( data["attribute"][i])-1]

    entrydata(data,"Brand",i)
    entrydatashoesize(data,"US Shoe Size",i)
    entrydata(data,"Style",i)
    entrydata(data,"Material",i)
    entrydata(data,"Country/Region of Manufacture",i)
    entrydata(data,"Width",i)


        
    
data[0:n].to_csv(r'C:\Users\HSU\Desktop\ML ebay\mlchallenge_set_2021.tsv\clean.csv')


# Date: 2020/11/27 Author: Yun Hung, Hsu
# If you want to change anything please put note and date on it

