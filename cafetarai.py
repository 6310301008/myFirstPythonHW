water = 400
milk= 540
coffee = 120
cups  = 9
money = 550

a = 1
while True:
    if a == 1:
        print(":" * 80)
        print("::"+ ' ' * 25+ "The Coffee machine has:"+ ' ' * 28  + "::")
        print('::'+ ' ' *76 + '::')
        print("::", ' ' * 29, (water), "ml. of water", ' ' * 27, "::")
        print('::'+ ' '*76 + '::')
        print('::'+ ' '*76 + '::')
        print('::'+ ' ' *76 + '::')
        print("::", ' ' * 29, (milk), "ml. of milk", ' ' * 28, "::")
        print('::'+ ' '*76 + '::')
        print('::'+ ' '*76 + '::')
        print('::'+ ' '*76 + '::')
        print("::", ' '* 29, (coffee), "g. of coffee beans", ' ' * 21, "::")
        print('::'+ ' '*76 + '::')
        print('::'+ ' '*76 + '::')
        print('::'+ ' '*76 + '::')
        print("::", ' ' *29, (cups), "of disposable cups", ' ' * 23, "::")
        print('::'+ ' ' *76 + '::')
        print('::'+ ' ' *76 + '::')
        print('::'+ ' ' *76 + '::')
        print("::", ' ' *29, (money), "$$$ of money", ' ' * 27, "::")
        print('::'+ ' '* 76 + '::')
        print('::'+ ' ' *76 + '::')
        print(":" * 80)
      

        b = input("choose one option - buy / fill/ take >")

        if "Buy" in b or "BUY" in b or "buy" in b:
            print(":" * 80)
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, "Choose Kind Of Coffee", ' ' * 26, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, "( 1 ) Espresso", ' ' * 33, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, "( 2 ) Latte", ' ' * 36, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, "( 3 ) Cappuccino", ' ' * 31, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(":" * 80)
            print(":" * 80)
            d = str(input(" do you want =>"))
            if 'espresso' in d or '1' in d:
                print(":" * 80)
                print("::", ' ' * 30, "Espresso", ' ' * 34, "::")
                print("::", ' ' * 27, "you pay 4 $$$", ' ' * 32, "::")
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    ": The Coffee machine has:",
                    ' ' * 22,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(water) - 250),
                    "ml. of water",
                    ' ' * 31,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print("::", ' ' * 25, (milk), "ml. of milk", ' ' * 32, "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(coffee) - 16),
                    "g. of coffee beans",
                    ' ' * 25,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(cups) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(money) + 4),
                    "$$$ of money",
                    ' ' * 31,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(":" * 80)
                print(":" * 80)
            elif 'latte' in d or '2' in d:
                print(":" * 80)
                print(":" * 80)
                print('::'+ ' '* 76 + '::')
                print("::", ' ' * 30, "Latte", ' ' * 37, "::")
                print("::", ' ' * 27, "you pay 7 $$$", ' ' * 32, "::")
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    "The Coffee machine has:",
                    ' ' * 24,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(water) - 350),
                    "ml. of water",
                    ' ' * 32,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(milk) - 75),
                    "ml. of milk",
                    ' ' * 32,
                    "::")
                print('::', ' ' * 74, '::')
                print('::', ' ' * 74, '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(coffee) - 20),
                    "g. of coffee beans",
                    ' ' * 25,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(cups) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(money) + 7),
                    "$$$ of money",
                    ' ' * 31,
                    "::")
                print('::'+ ' '* 76 + '::')
                print(":" * 80)
                print(":" * 80)
            elif 'cappuccino' in d or '3' in d:
                print(":" * 80)
                print(":" * 80)
                print('::'+ ' '* 76 + '::')
                print("::", ' ' * 30, "Cappuccino", ' ' * 32, "::")
                print("::", ' ' * 27, "*you pay 6 $$$", ' ' * 31, "::")
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    "The Coffee machine has:",
                    ' ' * 24,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(water) - 200),
                    "ml. of water",
                    ' ' * 31,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(milk) - 100),
                    "ml. of milk",
                    ' ' * 32,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(coffee) - 12),
                    "g. of coffee beans",
                    ' ' * 25,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(cups) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(
                    "::",
                    ' ' * 25,
                    (int(money) + 6),
                    "$$$ of money",
                    ' ' * 31,
                    "::")
                print('::'+ ' '* 76 + '::')
                print('::'+ ' '* 76 + '::')
                print(":" * 80)
                print(":" * 80)
            else:
                print("Stop Working")

        elif "fill" in b or "Fill" in b or "FILL" in b:
            waterfill = int(input(" how many ml of water:\n>"))
            milkfill = int(input(" how many ml of milk:\n>"))
            coffeefill = int(input("how many grams of coffee beans:\n>"))
            cupsfill = int(input("how many disposable cups :\n>"))

            print(":" * 80)
            print(":" * 80)
            print("::", ' ' * 30, ">Result<", ' ' * 34, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, ":The Coffee machine has:", ' ' * 23, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(water) + (waterfill)),
                "ml. of water",
                ' ' * 31,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(milk) + (milkfill)),
                "ml of milk",
                ' ' * 33,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(coffee) + (coffeefill)),
                "g. of coffee beans",
                ' ' * 25,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(cups) + (cupsfill)),
                "of disposable cups",
                ' ' * 26,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, (int(money)), "$$$ of money", ' ' * 31, "::")
            print('::'+ ' '* 76 + '::')
            print(":" * 80)
            print(":" * 80)
        elif "take" in b or "Take" in b or "TAKE" in b:
            print(":" * 80)
            print(":" * 80)
            print('::', ' ' * 74, '::')
            print(
                "::",
                ' ' * 25,
                "< I gave you ",
                (money),
                " $$$ > ",
                ' ' * 22,
                "::")
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 33, "Result", ' ' * 33, "::")
            print("::", ' ' * 25, " :The Coffee machine has:", ' ' * 22, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, (int(water)), "ml of water", ' ' * 32, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, (int(milk)), "ml of milk", ' ' * 33, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(coffee)),
                "g. of coffee beans",
                ' ' * 25,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(
                "::",
                ' ' * 25,
                (int(cups)),
                "of disposable cups",
                ' ' * 27,
                "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print("::", ' ' * 25, (int(money) - money), "$$$ of money", ' ' * 33, "::")
            print('::'+ ' '* 76 + '::')
            print('::'+ ' '* 76 + '::')
            print(":" * 80)
            print(":" * 80)
        else:
            print("Stop Working")

        x = input("Stop/Retrun : >")
        if "STOP" in x or "Stop" in x or "s" in x or "S" in x :
            x = 0
        elif "Retrun" in x or "retrun" in x or "R" in x or "r" in x:
            y = 1
        else:
            print("Stop working")
    elif x == 0:
        break
