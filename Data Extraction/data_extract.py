import pandas as pd
import re

data=pd.read_csv(r'C:\Users\HSU\Desktop\ML ebay\mlchallenge_set_2021.tsv\mlchallenge_set_2021.tsv',encoding = "ISO-8859-1", sep='\t',header=None )

data.columns=["Category","primary_image_url","all_image_url","attribute","index"]



n=10 #enter the number of data that want to extract

#add empty column
data["Brand"]=""
data["Color"]=""
data["US Shoe Size"]=""
data["Style"]=""
data["Material"]=""
data["Country/Region of Manufacture"]=""
data["Width"]=""

def entrydata(data,column,i):    #column is the colname datatype:string;
    
    a=re.search(column,data["attribute"][i])
    if(a==None):
        data[column][i]="N\A"
    else:
        loc=a.span()
        temp=data["attribute"][i][loc[1]+1:]
        a=re.search(',',temp)
        if(a==None):
            data[column][i]=temp
        else:
            loc=a.span()
            data[column][i]=temp[0:loc[0]]



def entrydatashoesize(data,column,i):    #column is the colname datatype:string;
    a=re.search(column,data["attribute"][i])
    if(a==None):
        data[column][i]="N\A"
    else:
        loc=a.span()
        temp=data["attribute"][i][loc[1]+9:]
        a=re.search(',',temp)
        if(a==None):
            data[column][i]=temp
        else:
            a=re.search(',',temp).span()
            data[column][i]=temp[0:a[0]]


    


for i in range(0,n):
    data["attribute"][i] =data["attribute"][i][1:]
    data["attribute"][i] =data["attribute"][i][0:len( data["attribute"][i])-1]

    entrydata(data,"Brand",i)
    entrydata(data,"Color",i)
    entrydatashoesize(data,"US Shoe Size",i)
    entrydata(data,"Style",i)
    entrydata(data,"Material",i)
    entrydata(data,"Country/Region of Manufacture",i)
    entrydata(data,"Width",i)


        
    
data[0:n].to_csv(r'C:\Users\HSU\Desktop\ML ebay\mlchallenge_set_2021.tsv\clean.csv')


# Date: 2020/11/27 Author: Yun Hung, Hsu
# If you want to change anything please put note and date on it

