import os
import time

def osszeadas(n1,n2):
    if n1 == x:
        if "." in str(n1) or "." in str(n2):
            y = float(n1) + float(n2)
            if str(y)[-1] == "0":
                return int(y)
            else:
                return y
        else:
            return int(n1) + int(n2)
    elif "." in str(n1) or "." in str(n2):
        return float(n1) + float(n2)
    else:
        return int(n1) + int(n2)

def kivonas(n1,n2):
    if n1 == x:
        if "." in str(n1) or "." in str(n2):
            y = float(n1) - float(n2)
            if str(y)[-1] == "0":
                return int(y)
            elif "999999" in str(y):
                return round(y)
            else:
                return y
        else:
            return int(n1) - int(n2)
    else:
        y = float(n1) - float(n2)
        if str(y)[-1] == "0":
            return int(y)
        elif str(y)[-1] == "5":
            return str(y)[:3]
        elif "999999" in str(y):
            return round(y)
        else:
            return y

def szorzas(n1,n2):
    if n1 == x:
        if "." in str(n1) or "." in str(n2):
            return float(n1) * float(n2)
        else:
            return int(n1) * int(n2)
    elif "." in str(n1) or "." in str(n2):
        return float(n1) * float(n2)
    else:
        return int(n1) * int(n2)

def osztas(n1,n2):
    if n1 == x:
        if "." in str(n1) or "." in str(n2):
            y = float(n1) / float(n2)
            return int(y)
        else:
            return int(n1) // int(n2)
    elif "." in n1 or "." in n2:
            return round((float(n1)) / (float(n2)),4)
            
    else:
        y = int(n1) // int(n2)
        return y

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

os.system('cls||clear')
while True:
    print("\nMit akarsz elvégezni? ")
    val = input("[1]osszeadas\n[2]kivonas\n[3]szorzas\n[4]osztas\n")
    
    if val == "1":
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = osszeadas(x,n2)
            print(x)  
        else:  
            n1 = input("Kérek egy számot: ")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = osszeadas(n1,n2)
            print(x) 
        ujrakezdes()
            
                
            
    elif val == "2":
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = kivonas(x,n2)
            print(x)  
        else:  
            n1 = input("Kérek egy számot: ")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = kivonas(n1,n2)
            print(x) 
        ujrakezdes()
                
            
    elif val == "3":
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = szorzas(x,n2)
            print(x)  
        else:  
            n1 = input("Kérek egy számot: ")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = szorzas(n1,n2)
            print(x) 
        ujrakezdes()
                
            
    elif val == "4":
        if x != "":
            print(f"Egyik számod: {x}")
            n2 = input("Kérek egy számot: ")
            print("A végeredmény: ")
            x = osztas(x,n2)
            print(x)  
        else:  
            n1 = input("Kérek egy számot: ")
            n2 = input("Kérek egy számot: ")
            if n2 == "0":
                print("\n0-val nem lehet osztani!")
                time.sleep(1)
                os.system('cls||clear')
                continue
            print("A végeredmény: ")
            x = osztas(n1,n2)
            print(x) 
        ujrakezdes()

    elif val == "end":
        print("Viszlát!")
        time.sleep(1)
        os.system('cls||clear')
        break
    
    else:
        print("Olyat válassz ami van")
        time.sleep(2)
        os.system('cls||clear')
