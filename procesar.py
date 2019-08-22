import pandas as pd
import xlrd 
from gestionapp.models import Pldatosreloj

def cargar_data(data):
       
    df = pd.read_excel (data) #for an earlier version of Excel, you may need to use the file extension of 'xls'
    #print (df)
    
    #data = pd.read_excel (r'C:\Users\Ron\Desktop\Product List.xlsx') 
    dc = pd.DataFrame(df, columns= ['Nombre','Fecha/Hora','No.','ID Equipo'])
    #print (dc)
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
    for row in dc.itertuples(name='pldatosreloj'):
        #pldatosreloj = Pldatosreloj.objects.create(name='pldatosreloj')
        print(row)


    
    #print(type(data))
    #print(data)
    print("2FIN")