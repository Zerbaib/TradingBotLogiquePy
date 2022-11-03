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
ntndo = 100
prixN = ntndo
#
 # # # Start Block


 # # # Block fontion
#
# Block fonction menu d'achat vente
def menuA():
    os.system("cls")
    choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
    if choix2 == "1":
        menuA1()
        
    if choix2 == "2":
        menuA2()

    if choix2 == "3":
        menuA3()

def menuA1():
    acht = input(f"que veux tu acheter ?\n1. Nintendo | prix: {ntndo}\n")
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
        os.system('cls')
def menuA2():
    vndr = input(f"que veut tu vendre ?\n1. Nintendo | prix: {ntndo}\n")
    if vndr == "1":
        if wallet.__contains__("ntndo") == True:
            nmbrVndr = input("commbien veut tu en vendre\n") # exemple 9
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
def menuA3():
    os.system("cls")
    print(f"dollars sur le compte: {usd}")
    print("vous possedez:")
    print("Nintendo: " + str(wallet.get("ntndo")))
    time.sleep(1.5)
    os.system("cls")
# Fin block fonction menu d'achat vente
#
 # # # Block fonction
while True:
    choix1 = input("que veux tu faire\n1. menu d'achat\n2. regarder les prix\n")
    
    if choix1 == "1":
        menuA()

    if choix1 == "2":
        for i in range(5):
            os.system("cls")
            prixN = ntndo
            ntndo = prixN + random.randint(-25, 250)

            if ntndo != prixN:
                if ntndo < prixN:
                    print(f"le prix de Nintendo est a {ntndo} $ | actuellement -")
                else:
                    print(f"le prix de Nintendo est a {ntndo} $ | actuellement +")
            else:
                print(f"le prix de Nintendo est a {ntndo} $ | actuellement =")
            time.sleep(1)
            os.system("cls")
    
    time.sleep(1)
    with open('wallet.txt', 'w') as file:
        json.dump(wallet, file)