def findIndexes(sheet):
    indexes=[]
    for col in range(sheet.ncols):
        # print(sheet.cell(0,col).value)
        if(sheet.cell(0,col).value.lower()=="transaction type"):
            indexes.append(["delivered",col])
        elif(sheet.cell(0,col).value.lower()=="ship to state"):
            indexes.append(["states",col])
        elif(sheet.cell(0,col).value.lower()=="tax exclusive gross"):
            indexes.append(["exclusiveGross",col])
    # print('Delivered index : [{}] , States index : [{}] , Tax Exclusive Gross index : [{}]'.format(delivered,states,exclusiveGross))
    # print(*indexes)
    return indexes

import xlrd
import os
import sys 
# location = ("E:\gstcalclubfact\order.xlsx")
location = os.getcwd()+"\order.xlsx"
# print(location) 
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
indexes = findIndexes(sheet)
deliveredIndex,stateIndex,exclusiveGrossIndex=-1,-1,-1
for i in indexes:
    if(i[0]=="delivered"):
        deliveredIndex=i[1]
    elif(i[0]=="states"):
        stateIndex=i[1]
    elif(i[0]=="exclusiveGross"):
        exclusiveGrossIndex=i[1]
if(deliveredIndex==-1 or stateIndex==-1 or exclusiveGrossIndex==-1):
    print(" Indexes not found index might not be present you are searching for ")
    sys.exit()
else:
    target,temp,final=[],[],[]
    for row in range(sheet.nrows):
    # for row in range(20):
        if sheet.cell(row,deliveredIndex).value == "Delivered":
            temp.append(sheet.cell(row,stateIndex).value)
            temp.append(sheet.cell(row,exclusiveGrossIndex).value)
            final.append(temp)
            temp=[]
    states=set()
    for i in final:
        states.add(i[0])
    states=list(states)
    states.sort()
 
    for i in states:
        x=0
        count=0
        for j in final:
            if j[0]==i:
                x+=j[1]
                count+=1
        target.append([i,x,count])
    print(*target,sep="\n")
    input()
