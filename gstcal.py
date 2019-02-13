import xlrd
location = ("E:\gstcalc\orders.xlsx")
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
report=[],temp=[],final=[]
for i in range(sheet.nrows):
    if sheet.cell(i,7).value == "Delivered":
        temp.append(sheet.cell(i,46).value)
        temp.append(sheet.cell(i,20).value)
        temp.append(sheet.cell(i,18).value)
        temp.append(sheet.cell(i,16).value)
        temp.append(sheet.cell(i,12).value)
        temp.append(sheet.cell(i,8).value)
        final.append(temp)
        temp=[] 
states=set()
selling_price,sgst,cgst,igst,seller_invoice_amount=0,0,0,0,0
for i in final:
    states.add(i[0])
states=list(states)
for i in states:
    target=""
    selling_price,sgst,cgst,igst,seller_invoice_amount=0,0,0,0,0
    for j in final:
        if i==j[0]:
            if j[1]=="":
                igst+=0
            else:
                igst+=float(j[1])
            if j[2]=="":
                cgst+=0
            else:
                cgst+=float(j[2])
            if j[3]=="":
                sgst+=0
            else:
                sgst+=float(j[3])
            if j[4]=="":
                seller_invoice_amount+=0
            else:
                seller_invoice_amount+=float(j[4])
            if j[5]=="":
                selling_price+=0
            else:
                selling_price+=float(j[5])
    target=str(i)+" "+"IGST: "+str(igst)+" "+"CGST: "+str(cgst)+" "+"SGST: "+str(sgst)+" "+"seller invoice amount: "+str(seller_invoice_amount)+" "+"Selling Price: "+str(selling_price)
    report.append(target)
for i in report:
    print(i)