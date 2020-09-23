y = 1
while True :
    if y == 1 :
        kittikhun = ('Kittikhuns gas station')
        print(kittikhun.upper() )

        today = (" Oil price today ")
        print(today.upper())

        Type_oli = [ " Gasoline 95 " , " Gasoline 91 " ," Gasohol 91 " , " Gasohol_E20 " , " Gasohol_95 " , " Diesel " ]
        Price_oli = [ 29.19 , 25.30 , 21.68 , 20.20 ,  21.20 , 21.10 ]
        for c in range ( len ( Type_oli ) )  :
            print ( str(c+1) + "." + Type_oli[c] + "  :|:  " + str( Price_oli[c]) +"  :|: " +" Baht per liter ")

        f = input ("Which type of fuel do you want to choose?  :  \n:<>: 1.Gasoline_95 \n:<>: 2.Gasoline_91 \n:<>: 3.Gasohol_91 \n:<>: 4.Gasohol_E20 \n:<>: 5.Gasohol_95 \n:<>: 6.Diesel   \n Want to choose  =>>> :   ")   
        e = input("Which one do you want to choose? : \n :<>: 1.Price_per_liter \n  :<>:  2.Liters_per_price  \n \n Want to choose   =>>>  : ")


        if "1" in e :
            n1 = input (" Amount to be entered     \n Money entered  =>>> :   ")
            g1 = int( n1 )

        elif "2" in e :
            n2 = input (" Required number of liters     \n Number of liters put  =>>> :   ")
            g2 = int ( n2 ) 

        else : 
            print("   No data found   please go back and choose again  ")


        if "1"  in e  :

            if '1'  in f  :
                u = ( g1 / 29.16 )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            elif '2'   in f :
                u = ( g1 / 25.30  )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            elif '3'   in f :
                u = ( g1 / 21.68  )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            elif '4'   in f :
                u = ( g1 / 20.2  )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            elif '5'   in f :
                u = ( g1 / 21.2  )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            elif '6'   in f :
                u = ( g1 / 21.1  )
                print ("Amount of fuel received =>>:  ", '%.2f' %u ," liters " )

            else :
                print("The information is incorrect, please check again")


        elif "2" in e :

            if '1'  in f  :
                u = ( g2 * 29.16 )
                print ("Total amount =>>:  ", u ,"Baht " )

            elif '2'   in f :
                u = ( g2 * 25.30  )
                print ("Total amount =>>:  ", u ," Baht " )

            elif '3'   in f :
                u = ( g2 * 21.68  )
                print ("Total amount =>>:  ", u ," Baht " )

            elif '4'   in f :
                u = ( g2 * 20.2  )
                print ("Total amount =>>:  ", u ," Baht " )

            elif '5'   in f :
                u = ( g2 * 21.2  )
                print ("Total amount =>>:  ", u ," Baht " )

            elif '6'   in f :
                u = ( g2 * 21.1  )
                print ("Total amount =>>:  ",  u ,"Baht " )

            else :
                print("The information is incorrect, please check again")

        x = int(input("Chosse 1 for to work  Chosse 0 for Stop working"))
        y = x
    elif y == 0:
        print(" Stop working ")
        break
 
