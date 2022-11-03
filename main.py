 # # # Block module
#
import random
from socketserver import UDPServer
import time
import os
import json
from xml.dom.domreg import well_known_implementations
#
 # # # Block module

 # # # Start Block
#
with open('wallet.txt', 'r') as file:
    wallet = json.load(file)
with open('price.txt','r') as file:
    price = json.load(file)

usd = wallet.get("usd")
ntndo = price.get("ntndo")
prixN = ntndo

apl = price.get("apl")
prixA = apl

chnl = price.get("chnl")
prixC = chnl
#
 # # # Start Block


 # # # Block fontion
#
# Block fonction menu d'achat vente
def menuA():
    os.system("cls")
    choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
    if choix2 == "1":
        menuA1(ntndo, apl, chnl, usd)
        
    if choix2 == "2":
        menuA2(ntndo, apl, chnl, usd)

    if choix2 == "3":
        menuA3()

def menuA1(ntndo, apl, chnl, usd):
    acht = input(f"que veux tu acheter ?\n1. Nintendo | prix: {ntndo}\n2. Apple | prix: {apl}\n3. Channel | prix {chnl}\n")
    if acht == "1":
        nombreA = input("combient en veux tu ?\n")
        nombreA = int(nombreA)
        ntndo = int(price.get("ntndo"))
        prixT =  ntndo*nombreA
        prixT = int(prixT)
        usd = int(usd)
        if usd >= prixT:
            wallet["ntndo"] = nombreA
            print(f"vous avez bien acheter {nombreA} d'action Nintendo pour le prix de {prixT}")
            usd = int(usd)
            prixT = int(prixT)
            usd = usd - prixT
            wallet["usd"] = usd
            time.sleep(1)
        else:
            print("vous avez pas assez")
            time.sleep(0.5)
        os.system('cls')
    if acht == "2":
        nombreB = input("combient en veux tu ?\n")
        nombreB = int(nombreB)
        apl = int(price.get("apl"))
        prixT = apl*nombreB
        prixT = int(prixT)
        usd = int(usd)
        if usd >= prixT:
            wallet["apl"] = nombreB
            print(f"vous avez bien acheter {nombreB} d'action Apple pour le prix de {prixT}")
            usd = int(usd)
            prixT = int(prixT)
            usd = usd - prixT
            wallet["usd"] = usd
            time.sleep(1)
        else:
            print("vous avez pas assez")
            time.sleep(0.5)
        os.system('cls')
    if acht == "3":
        nombreC = input("combient en veux tu ?\n")
        nombreC = int(nombreC)
        chnl = int(price.get("chnl"))
        prixT = chnl*nombreC
        prixT = int(prixT)
        usd = int(usd)
        if usd >= prixT:
            wallet["chnl"] = nombreC
            print(f"vous avez bien acheter {nombreC} d'action Channel pour le prix de {prixT}")
            usd = int(usd)
            prixT = int(prixT)
            usd = usd - prixT
            wallet["usd"] = usd
            time.sleep(1)
        else:
            print("vous avez pas assez")
            time.sleep(0.5)
        os.system('cls')
def menuA2(ntndo, apl, chnl, usd):
    vndr = input(f"que veut tu vendre ?\n1. Nintendo | prix: {ntndo}\n2. Apple | prix: {apl}\n3. Channel | prix: {chnl}\n")
    if vndr == "1":
        if wallet.__contains__("ntndo") == True:
            if wallet.get("ntndo") != 0:
                nmbrVndr = input("combien veut tu en vendre\n")
                nmbrVndr = int(nmbrVndr)
                usd = int(usd)
                if wallet.get("ntndo") >= nmbrVndr:
                    wallet["ntndo"] = wallet.get("ntndo") - nmbrVndr
                    tmp = nmbrVndr * price.get("ntndo")
                    usd = usd + tmp
                    wallet["usd"] = usd
                    print(f"vous avez bien vendue {nmbrVndr} pour le prix de {tmp}")
                    print(f"vous avez maintenent {usd} $ dans votre compte")
                else:
                    print("vous avez pas asser")
                time.sleep(1)
            else:
                print("vous en avez 0")
                time.sleep(0.5)
        else:
            print("ERROR 101")
            time.sleep(0.5)
        os.system("cls")
    if vndr == "2":
        if wallet.__contains__("apl") == True:
            if wallet.get("apl") != 0:
                nmbrVndr = input("combien veut tu en vendre\n")
                nmbrVndr = int(nmbrVndr)
                usd = int(usd)
                if wallet.get("apl") >= nmbrVndr:
                    wallet["apl"] = wallet.get("apl") - nmbrVndr
                    tmp = nmbrVndr * price.get("apl")
                    usd = usd + tmp
                    wallet["usd"] = usd
                    print(f"vous avez bien vendue {nmbrVndr} pour le prix de {tmp}")
                    print(f"vous avez maintenent {usd} $ dans votre compte")
                else:
                    print("vous avez pas asser")
                time.sleep(1)
            else:
                print("vous en avez 0")
                time.sleep(0.5)
        else:
            print("ERROR 101")
            time.sleep(0.5)
        os.system("cls")
    if vndr == "3":
        if wallet.__contains__("chnl") == True:
            if wallet.get("chnl") != 0:
                nmbrVndr = input("combien veut tu en vendre\n")
                nmbrVndr = int(nmbrVndr)
                usd = int(wallet.get("usd"))
                if wallet.get("chnl") >= nmbrVndr:
                    wallet["chnl"] = wallet.get("chnl") - nmbrVndr
                    tmp = nmbrVndr * price.get("chnl")
                    usd = usd + tmp
                    wallet["usd"] = usd
                    print(f"vous avez bien vendue {nmbrVndr} pour le prix de {tmp}")
                    print(f"vous avez maintenent {usd} $ dans votre compte")
                else:
                    print("vous avez pas asser")
                time.sleep(1)
            else:
                print("vous en avez 0")
                time.sleep(0.5)
        else:
            print("ERROR 101")
            time.sleep(0.5)
        os.system("cls")
def menuA3():
    os.system("cls")
    print(f"dollars sur le compte: " + str(wallet.get("usd")))
    print("vous possedez:")
    print("Nintendo: " + str(wallet.get("ntndo")))
    print("Apple: " + str(wallet.get("apl")))
    print("Channel: " + str(wallet.get("chnl")))
    time.sleep(1.5)
    os.system("cls")
# Fin block fonction menu d'achat vente

# Block fonction prix
def prixCA():
    for i in range(5):
        os.system("cls")
        nintendo(ntndo)
        apple(apl)
        channel(chnl)
        time.sleep(1)
        os.system("cls")
# Fin block fonction prix

# Block fonction marque
def nintendo(ntndo):
    prixN = ntndo
    ntndo = prixN + random.randint(-100, 100)
    if ntndo != prixN:
        if ntndo < prixN:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement -")
        else:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement +")
    else:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement =")
    price["ntndo"] = ntndo
def apple(apl):
    prixA = apl
    apl = prixA + random.randint(-100, 100)
    if apl != prixA:
        if apl < prixA:
            print(f"le prix de Apple est a {apl} $ | actuellement -")
        else:
            print(f"le prix de Apple est a {apl} $ | actuellement +")
    else:
        print(f"le prix de Apple est a {apl} $ | actuellement =")
    price["apl"] = apl
def channel(chnl):
    prixC = chnl
    chnl = prixA + random.randint(-100, 100)
    if chnl != prixC:
        if chnl < prixC:
            print(f"le prix de Channel est a {chnl} $ | actuellement -")
        else:
            print(f"le prix de Channel est a {chnl} $ | actuellement +")
    else:
        print(f"le prix de Channel est a {chnl} $ | actuellement =")
    price["chnl"] = chnl
# Fin block fonction marque
#
 # # # Block fonction

 # # # Block boucle
#
while True:
    choix1 = input("que veux tu faire\n1. menu d'achat\n2. regarder les prix\n")
    
    if choix1 == "1":
        menuA()

    if choix1 == "2":
        prixCA()
    
    time.sleep(1)
    with open('wallet.txt', 'w') as file:
        json.dump(wallet, file)
    with open('price.txt', 'w') as file:
        json.dump(price, file)
#
 # # # Block boucle