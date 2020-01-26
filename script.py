import psycopg2 as ps
import pandas as pd 
import json 
import requests

url = "API_destination/"

headers = {
    'key': "api_key",
    'clientid': "client"
    }
r=requests.get(url, headers=headers)
data=r.json()

customers = data['json_object']

df=pd.DataFrame(json_object)
df.head()

def store_data(var1,var2,...):
    db=ps.connect(dbname="dbname", user="user", password="password", host="host", port="port")
    cursor = db.cursor()
    insert_query = "Insert INTO customers2 (var1,var2,...) VALUES (%s, %s, ...)"
    cursor.execute(insert_query, (var1,var2,..)
    cur.commit()
    cur.close
    return 

print('data sending to database')
for i in range (len(customers)):
    var1=customers[i]['var1']
    var2=customers[i]['city']
  

    store_data(var1,var2,...)
print('data is sent to database')
