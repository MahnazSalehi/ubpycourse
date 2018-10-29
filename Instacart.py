import csv
import datetime
a = datetime.datetime.now()
file=open( "orders.CSV", "r")
reader = csv.reader(file)
#list1 = []
c0=c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=c13=c14=c15=c16=c17=c18=c19=c20=c21=c22=c23=0
for line in reader:
    t=line[5]
    if t == '00':
        c0=c0+1
    if t == '01':
        c1=c1+1
    if t == '02':
        c2=c2+1
    if t == '03':
        c3=c3+1
    if t == '04':
        c4=c4+1
    if t == '05':
        c5=c5+1
    if t == '06':
        c6=c6+1
    if t == '07':
        c7=c7+1
    if t == '08':
        c8=c8+1
    if t == '09':
        c9=c9+1
    if t == '10':
        c10=c10+1
    if t == '11':
        c11=c11+1
    if t == '12':
        c12=c12+1
    if t == '13':
        c13=c13+1
    if t == '14':
        c14=c14+1
    if t == '15':
        c15=c15+1
    if t == '16':
        c16=c16+1
    if t == '17':
        c17=c17+1
    if t == '18':
        c18=c18+1
    if t == '19':
        c19=c19+1
    if t == '20':
        c20=c20+1
    if t == '21':
        c21=c21+1
    if t == '22':
        c22=c22+1
    if t == '23':
        c23=c23+1
ave=(c0+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23)/24
b = datetime.datetime.now()
c = b - a
print("The Time required to calcute (Sec):",int(c.total_seconds()),"The Average amount of orders placed during each hour of day :",ave,"Hour 00:",c0,"Hour 01:",c1,"Hour 02:",c2,
      "Hour 03:",c3,"Hour 04:",c4,"Hour 05:",c5,"Hour 06:",c6,"Hour 07:",c7,"Hour 08:",c8,"Hour 09:",c9,"Hour 10:",c10,
      "Hour 11:",c11,"Hour 12:",c12,"Hour 13:",c13,"Hour 14:",c14,"Hour 15:",c15,"Hour 16:",c16,"Hour 17:",c17,
      "Hour 18:",c18,"Hour 19:",c19,"Hour 20:",c20,"Hour 21:",c21,"Hour 22:",c22,"Hour 23:",c23,sep='\n')