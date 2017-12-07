# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by Aaron Albert for COMP9021

import sys
import os
import csv
from collections import defaultdict

Con_Values=[]
agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
con = []
ag1_val= []
ag2_val= []
ag_dict={}
year_1, year_2 = None, None
l=list(years)
if l[0] > l[1]:
    year_1=l[1]
    year_2=l[0]
else:
    year_1=l[0]
    year_2=l[1]

# Insert your code here
#Agricultural Land
rownum=0
f=open(agricultural_land_filename,'r',encoding='utf-8')
reader=csv.reader(f)
for row in reader:
    if rownum==4:
         index1=row.index(str(year_1))
         index2=row.index(str(year_2))
    if rownum > 4:
        con.append(row[0])
        ag1_val.append(row[index1])
        ag2_val.append(row[index2]) 
    rownum+=1
 
f.close()
#Dictionary For Agrcultural Land values
for i in range(0,len(ag1_val)):
    if str(ag1_val[i])=='' or str(ag2_val[i])=='':
        continue
    elif float(ag1_val[i]) > float(ag2_val[i]):
        continue
    else:
        ag_dict[con[i]]=(float(ag2_val[i])-float(ag1_val[i]))        
#print(ag_dict) 

 #Forest Land
fl1_val=[]
fl2_val=[]
fl_dict={}
rownum1=0
g=open(forest_filename,'r',encoding='utf-8')
reader=csv.reader(g)
for row in reader:
    if rownum1==4:
         index1=row.index(str(year_1))
         index2=row.index(str(year_2))
    if rownum1 > 4:
        fl1_val.append(row[index1])
        fl2_val.append(row[index2]) 
    rownum1+=1
g.close()
#Dictionary For Forest Land values
for i in range(0,len(fl1_val)):
    if str(fl1_val[i])=='' or str(fl2_val[i])=='':
        continue
    elif float(fl1_val[i]) > float(fl2_val[i]):
        continue
    else:
        fl_dict[con[i]]=(float(fl2_val[i])-float(fl1_val[i]))
#print(fl_dict)

#Ratio
ratio_fin={}
for i in range(0,len(con)):
    if con[i] in ag_dict and con[i] in fl_dict:
        val1=ag_dict[con[i]]
        val2=fl_dict[con[i]]
        if val2==0.0:
            continue
        else:
            ratio_fin[con[i]]=round((val1/val2),2)
    else:
        continue
 
sortedCountries= sorted([[value,key] for (key,value) in ratio_fin.items()],reverse=True)

Con_Values=sortedCountries[0:top_n]

for i in range(0,len(Con_Values)):
    Countries=Con_Values[i][1]
    Values=str(f'{Con_Values[i][0]:.2f}')
    str1=Countries+' '+'('+Values+')'
    countries.append(str1)
    
print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    