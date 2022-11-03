 # # # Block module
#
import random
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

usd = wallet.get("usd")
ntndo = 173
prixN = ntndo

apl = 251
prixA = apl
#
 # # # Start Block


 # # # Block fontion
#
# Block fonction menu d'achat vente
def menuA():
    os.system("cls")
    choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
    if choix2 == "1":
        menuA1(ntndo, apl, usd)
        
    if choix2 == "2":
        menuA2(ntndo, apl, usd)

    if choix2 == "3":
        menuA3(ntndo, apl, usd)

def menuA1(ntndo, apl, usd):
    acht = input(f"que veux tu acheter ?\n1. Nintendo | prix: {ntndo}\n2. Apple | prix: {apl}\n")
    if acht == "1":
        nombreA = input("combient en veux tu ?\n")
        nombreA = int(nombreA)
        ntndo = int(ntndo)
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
        apl = int(apl)
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
def menuA2(ntndo, apl, usd):
    vndr = input(f"que veut tu vendre ?\n1. Nintendo | prix: {ntndo}\n2. Apple | prix: {apl}\n")
    if vndr == "1":
        if wallet.__contains__("ntndo") == True:
            if wallet.get("ntndo") != 0:
                nmbrVndr = input("combien veut tu en vendre\n")
                nmbrVndr = int(nmbrVndr)
                usd = int(usd)
                if wallet.get("ntndo") <= nmbrVndr:
                    wallet["ntndo"] = wallet.get("ntndo") - nmbrVndr
                    tmp = nmbrVndr * ntndo
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
                if wallet.get("apl") <= nmbrVndr:
                    wallet["apl"] = wallet.get("apl") - nmbrVndr
                    tmp = nmbrVndr * apl
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
def menuA3(ntndo, apl, usd):
    os.system("cls")
    print(f"dollars sur le compte: " + str(wallet.get("usd")))
    print("vous possedez:")
    print("Nintendo: " + str(wallet.get("ntndo")))
    print("Apple: " + str(wallet.get("apl")))
    time.sleep(1.5)
    os.system("cls")
# Fin block fonction menu d'achat vente

# Block fonction prix
def prixC():
    for i in range(5):
        os.system("cls")
        nintendo(ntndo)
        apple(apl)
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
def apple(apl):
    prixA = apl
    apl = prixA + random.randint(-200, 200)
    if apl != prixA:
        if apl < prixA:
            print(f"le prix de Apple est a {apl} $ | actuellement -")
        else:
            print(f"le prix de Apple est a {apl} $ | actuellement +")
    else:
        print(f"le prix de Apple est a {apl} $ | actuellement =")
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
        prixC()
    
    time.sleep(1)
    with open('wallet.txt', 'w') as file:
        json.dump(wallet, file)
#
 # # # Block boucle