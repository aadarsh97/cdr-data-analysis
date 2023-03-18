import pandas as pd
from csv import reader,writer
import random as rand
location = pd.read_csv('c:\\Users\\ASTRA\\Desktop\\cdr\\location.csv') # csv file containing time and location
cdr = pd.read_csv('c:\\Users\\ASTRA\\Desktop\\oldcdr.csv') #csv file which is to be updated

a = len(cdr)

latitude = ["latitude"]
longitude= ["longitude"]
time = ['time_stamp']
age = ['age']

for i in range(0,a):     
    b = len(location)         
    random = rand.randint(0, b-1)
    x = location.iloc[random]
    lat = x.lat
    long = x.long
    tim = x.time
    ag = rand.randint(15, 50)
    latitude.append(lat)
    longitude.append(long)
    time.append(tim)
    age.append(ag)
    
input_file=   'cdrdata.csv'
output_file=  'enriched_data.csv'

col_1 = latitude
col_2 = longitude
col_3 = time
col_4 = age
    
with open(input_file, 'r') as read_obj,open(output_file, 'w', newline='') as write_obj:
  csv_reader = reader(read_obj)
  csv_writer = writer(write_obj)
  
  for row in csv_reader:
      
      row.append (col_1 [csv_reader.line_num-1] )
      row.append (col_2 [ csv_reader.line_num-1] ) 
      row.append (col_3 [csv_reader.line_num-1] )
      row.append (col_4 [csv_reader.line_num-1] )
      csv_writer.writerow(row)
      
      
       
