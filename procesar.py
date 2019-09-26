import pandas as pd
import xlrd 
from gestionapp.models import Pldatosreloj,Pltareosemanal
import math
from datetime import datetime

import time


def cargar_data(data):
       
    df = pd.read_excel (data) #for an earlier version of Excel, you may need to use the file extension of 'xls'
   
    #data = pd.read_excel (r'C:\Users\Ron\Desktop\Product List.xlsx') 
    dc = pd.DataFrame(df, columns= ['Nombre','Fecha/Hora','No.','ID Equipo'])
    
    #print (dc)
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
    # changing cols with rename() 
    new_data = dc.rename(columns = {"Nombre": "nombre", "No.":"codemp", "Fecha/Hora":"fecha"}) 
    
    #p = Pldatosreloj(codigo='Petr', codemp='xx')
    #p.save()
  
    
    #dfin = new_data[ ['codigo', 'codemp'] ]
    print("------INICIA for")
    #importar index sacar Rango de Fecha a Importar
    xmaster = 2

    Pldatosreloj.objects.filter(master=xmaster).delete()
    dateformat = "%m/%d/%Y"
    #07:00 - 8.05
    semana = Pltareosemanal.objects.get(id=xmaster)
    print ('semana.fechaini',semana.fechaini,semana.fechafin)
    
    horacero = datetime.strptime('00:00', '%H:%M').time()
    horainiciomax = datetime.strptime('08:05', '%H:%M').time()
    
    
    horarefriinimin = datetime.strptime('12:45', '%H:%M').time()
    horarefriinimax = datetime.strptime('13:35', '%H:%M').time()
    
    horarefrifinmin = datetime.strptime('13:45', '%H:%M').time()
    horarefrifinmax = datetime.strptime('15:15', '%H:%M').time()

    horasalidamin = datetime.strptime('17:25', '%H:%M').time()
    horasalidamax = datetime.strptime('19:45', '%H:%M').time()
    
    
    #11pm 8am
    resumen_horas = {}
    registro_resumen = []
    hr1=hr2=hr3=hr4 = horacero
    for row in new_data.itertuples(name='Pldatosreloj'):
        x = float(row[3])
        cdni    = row[3] if type(row[3]) == float and not math.isnan(x) else 0.00
        cnombre = row[1] if type(row[1]) == str else ''
        
        if str( row[2] ) != 'NaT':
            rfecha = row[2]
            dfecha= (rfecha.date())
            dhora= (rfecha.time())
            #horainicio = datetime.strptime('03:55', '%H:%M').time()
            #print (cnombre,int(cdni))
            cfecha = dfecha.strftime("%d/%m/%Y")
            chora = dhora.strftime("%H:%M")
            #dic_sumdetailprod[key] = [resdet['codpro']
            xconcepto="NOREGIS"
            if dhora<=horainiciomax:
               #print ("ENTRADA",cnombre,dfecha,dhora,int(cdni),dhora)
               xconcepto="ENTRADA"
               hr1=chora
            if horarefriinimin <= dhora <=horarefriinimax:
               #print ("DESCANI",cnombre,dfecha,dhora,int(cdni),dhora)
               xconcepto="ALMUERI"
               hr2=chora
            if horarefrifinmin <= dhora <=horarefrifinmax:
               #print ("DESCANF",cnombre,dfecha,dhora,int(cdni),dhora)
               xconcepto="ALMUERF"
               hr3=chora
            if horasalidamin <= dhora <=horasalidamax:
               #print ("SALIDAF",cnombre,dfecha,dhora,int(cdni),dhora)
               xconcepto="SALIDAF"
               hr4=chora
                
            #key = xconcepto+'-'+str(int(cdni)) +'-'+ cfecha +'-'+ chora
            key = str(int(cdni)) +'-'+ cfecha
            #print (key,dhora)
            #(df['birth_date'] > start_date) & (df['birth_date'] <= end_date)
            if dfecha >= semana.fechaini and dfecha <= semana.fechafin:
               resumen_horas[key] = [int(cdni), int(cdni), cnombre, dfecha, dfecha, hr1, hr2 , hr3, hr4 ]
               #print ('dfecha', dfecha,semana.fechaini,semana.fechafin)
            
            #p = Pldatosreloj (codigo=int(cdni),codemp=int(cdni),nombre=cnombre,fechaini=dfecha)
           
            #p.save()
    
    for item in resumen_horas.items():
        #print ('codigo:',item[1][1],'nombre:',item[1][2],item[1][3],item[1][4],item[1][5],item[1][6],item[1][7],item[1][8])
        time1 = datetime.strptime(item[1][5],'%H:%M')
        time2 = datetime.strptime(item[1][8],'%H:%M')
        ctothoras = str(time2-time1)[:-3]

        #ctothoras = '07:25'
        #print(ctothoras)


        infdetalle = Pldatosreloj.objects.create(codigo=item[1][1], codemp=item[1][1],
        nombre=item[1][2],fechaini=item[1][3],fechafin=item[1][4],
        hrentrada=item[1][5],hrinidesc=item[1][6],hrfindesc=item[1][7],hrsalida=item[1][8],
        hrtotal=ctothoras)
        # Agrega en Semana y en detalle movreloj se declara al inicio
        semana.movreloj.add(infdetalle)


   
   #  semana = Pltareosemanal.objects.get(id=1)
   #  infdetalle = Pldatosreloj.objects.create(codigo=int(cdni))
   #  print ("infdetalle",infdetalle)
   #  semana.movreloj.add(infdetalle)
   #  items2 = Pltareosemanal.objects.all().count()
   #  print('Items Luego',items2)
    print("2FIN")