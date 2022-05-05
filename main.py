import os, time

def bekeres():
    x = input("Válassz egy műveletet: ")
    if x == "1":
        osszeadas(input("Első számod: "), input("Második számod: "))
    elif x == "2":
        kivonas(input("Első számod: "), input("Második számod: "))

    elif x == "3":
        szorzas(input("Első számod: "),input("Második számod: "))

    elif x == "4":
        osztas(input("Első számod: "), input("Második számod: "))
    else:
        print("Olyat válassz ami van!")

def osszeadas(n1,n2):
    if "." in n1 or "." in n2:
        print(float(n1)+float(n2))
    else:
        print(int(n1)+int(n2))

def kivonas(n1,n2):
    if "." in n1 or "." in n2:
        print(float(n1)-float(n2))
    else:
        print(int(n1)-int(n2))

def szorzas(n1,n2):
    if "." in n1 or "." in n2:
        print(float(n1)*float(n2))
    else:
        print(int(n1)*int(n2))

def osztas(n1,n2):
    if "." in n1 or "." in n2:
        print(float(n1)/float(n2))
    else:
        print(int(n1)/int(n2))

while True:
    print("1;osszeadas\n2;kivonas\n3;szorzas\n4;osztas")
    bekeres()
    time.sleep(1)
    os.system('cls||clear')
