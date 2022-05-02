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

def ujrakezdes():
    v = int(input("Új művelet vagy folytatás?[1/2]"))
    if v == 1:
        os.system('cls||clear')
        global x
        x = ""
    if v == 2:
        os.system('cls||clear')
        print(f"Legutóbbi számod: {x}")
        print("Várom a következő műveletet!")

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
        else:  
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osszeadas(n1,n2)
            print(x) 
        ujrakezdes()
            
                
            
    elif val == 2:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = kivonas(x,n2)
            print(x)  
        else:  
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = kivonas(n1,n2)
            print(x) 
        ujrakezdes()
                
            
    elif val == 3:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = szorzas(x,n2)
            print(x)  
        else:  
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = szorzas(n1,n2)
            print(x) 
        ujrakezdes()
                
            
    elif val == 4:
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osztas(x,n2)
            print(x)  
        else:  
            n1 = int(input("Kérek egy számot: "))
            n2 = int(input("Kérek egy számot: "))
            print("A végeredmény: ")
            x = osztas(n1,n2)
            print(x) 
        ujrakezdes()

    else:
        print("Olyat válassz ami van")
        time.sleep(2)
        os.system('cls||clear')
