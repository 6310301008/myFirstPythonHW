import json
import xmltodict
from suds.client import Client
price_oil = {"Gasoline 95": 29.16,
             "Gasoline 91": 25.30,
             "Gasohol 91": 21.68,
             "Gasohol E20": 20.2,
             "Gasohol 95": 21.2,
             "Diesel": 21.2}

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')

OilPrice1 = xmltodict.parse(OilPrice)  # ได้ผลลัพธ์เป็น json ในสตริง
Price = eval(json.dumps(OilPrice1))  # เรียกใช้งาน json ในสตริง
print(Price)

for i in Price["PTTOR_DS"]["FUEL"]:
    if ("PRICE" in i):
        price_oil[i["PRODUCT"]] = float(i["PRICE"])
y = 1
while True:
    if y == 1:
        print(':'*80)
        print(':'*80)
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*20 + 'WELCOM TO THE KITTIKHUN GASSTATION' + ' '*20 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print(':'*80)
        print(':'*80)
        print(' '*80)
        print("+"*80)
        print(' '*80)
        print(':'*80)
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*30 + 'Oil price today' + ' '*31 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*24 + "1.Gasoline 95 price" + ' ' + ' %.2f' % (price_oil["Gasoline 95"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*24 + "2.Gasoline 91 price" + ' ' + ' %.2f' % (price_oil["Gasoline 91"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*24 + "3.Gasohol 91  price" + ' ' + ' %.2f' % (price_oil["Gasohol 91"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*24 + "4.Gasohol E20 price" + ' ' + ' %.2f' % (price_oil["Gasohol E20"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*24 + "5.Gasohol 95  price" + ' ' + ' %.2f' % (price_oil["Gasohol 95"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*24 + "6.Diesel      price" + ' ' + ' %.2f' % (price_oil["Diesel"]) + ' '+'Baht' + ' '*21 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print(":"*80)
        o = 0
        while not (o in ['1', '2', '3', '4', '5', '6']):
            f = input("  : \n Want to choose  =>>> :   ")
            o = f
        print(':'*80)
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*32 + 'Choose of kicking money' + ' '*21 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*24 + '1.Price reduced in liters' + ' '*27 + '::')
        print('::' + ' '*24 + '2.The number of liters is the price' + ' '*17 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print('::' + ' '*76 + '::')
        print(':'*80)
        print(':'*80)
        
        l1 = 0
        status = True
        a = 0
        while not (l1 in ['1', '2']):
            if l1 in ['1', '2'] and status == True:
                status = True
            else:
                status = False
                if a > 0:
                    print('new choose')
            a += 1
            l1 = input(
                "do you want to choose? : \n Want to choose   =>>>  : ")
            e = l1
        if "1" in e:
            n1 = input(" Amount to be entered     \n Money entered  =>>> :   ")
            g1 = int(n1)

        elif "2" in e:
            n2 = input(
                " Required number of liters \n Number of liters put  =>>> :   ")
            g2 = int(n2)

        if "1" in e:
            if '1' in f:
                u = (g1 / price_oil["Gasoline 95"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '2' in f:
                u = (g1 / price_oil["Gasoline 91"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '3' in f:
                u = (g1 / price_oil["Gasohol 91"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '4' in f:
                u = (g1 / price_oil["Gasohol E20"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '5' in f:
                u = (g1 / price_oil["Gasohol 95"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '6' in f:
                u = (g1 / price_oil["Diesel"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + 'Amount of fuel =>>:', '%.2f' %
                      u, 'liters' + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            else:
                print("The information is incorrect, please check again")

        elif "2" in e:

            if '1' in f:
                u = (g2 * price_oil["Gasoline 95"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '2' in f:
                u = (g2 * price_oil["Gasoline 91"])
                print(
                    ':'*80)
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '3' in f:
                u = (g2 * price_oil["Gasohol 91"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '4' in f:
                u = (g2 * price_oil["Gasohol E20"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '5' in f:
                u = (g2 * price_oil["Gasohol 95"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            elif '6' in f:
                u = (g2 * price_oil["Diesel"])
                print(':'*80)
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*20 + "Total amount :  ", '%.2f' %
                      u, "Baht " + ' '*24 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print('::' + ' '*76 + '::')
                print(':'*80)

            else:
                print("The information is incorrect, please check again")

            x = int(input("Chose 1 for to work  Chose 0 for Stop working\n"))
            y = x
    elif y == 0:
        print(" Stop working ")
        break


        
    
    
    
    
