import sqlalchemy
import pyodbc
import pandas as pd
import urllib
#engine = sqlalchemy.create_engine("mssql+pyodbc://u21a20:avl@1234567890@localhost/ReportServer?driver=SQL Server Native Client 11.0")

engine = sqlalchemy.create_engine('mssql+pyodbc://INGURWD110144/ReportServer?Driver=SQL Server Native Client 11.0')

df = pd.read_csv('C:\\Users\\u21a20\\Desktop\\itc.csv')
df.to_sql('gas_pems_table',engine,if_exists='append')

print('Connection established')
# write the DataFrame to a table in the sql database
#df.to_sql("table_name", engine)