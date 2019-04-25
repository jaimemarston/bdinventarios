import sqlite3
import pandas as pd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

filename="E:\proyectosdjango\Insumos_app_inventarios\PRUEBA.xlsx"
#con=sqlite3.connect('dbinventario.sqlite3')

con = sqlite3.connect("dbinventario.sqlite3")
 
df = pd.read_excel(filename, sheet_name='Sheet1')
print("Column headings:")
print(df.columns)

df.to_sql('gestionapp_articulo',con,if_exists='append', index=False)
con.commit()
con.close()



#wb=pd.read_excel(filename,sheet_name='hoja1')
#for sheet in wb:
#    wb[sheet].to_sql(sheet,con, index=False)
