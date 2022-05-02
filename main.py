import os
import time

def osszeadas(n1,n2):
    return n1 + n2

def kivonas(n1,n2):
    return n1 - n2

def szorzas(n1,n2):
    return n1 * n2

def osztas(n1,n2):
    return n1 // n2

x = ""

while True:
    print("\nMit akarsz elvégezni? ")
    val = int(input("[1]osszeadas\n[2]kivonas\n[3]szorzas\n[4]osztas\n"))
    if val == 1:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osszeadas(x,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
        else:
            
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osszeadas(n1,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
                
            
    elif val == 2:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = kivonas(x,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
        else:
            
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = kivonas(n1,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
                
            
    elif val == 3:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = szorzas(x,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
        else:
            
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = szorzas(n1,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
                
            
    elif val == 4:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osztas(x,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
        else:
            
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osztas(n1,n2)
            print(x)
            folyt = int(input("Új művelet vagy folytatás?[1/2]"))
            if folyt == 1:
                os.system('cls||clear')
                x = ""
            else:
                os.system('cls||clear')
                print(f"Legutóbbi számod: {x}")
                print("Várom a következő műveletet!")
        
    else:
        print("Olyat válassz ami van")
        time.sleep(2)
        os.system('cls||clear')