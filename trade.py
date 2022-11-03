import random
import time
import os
import json
from xml.dom.domreg import well_known_implementations

with open('wallet.txt', 'r') as file:
    wallet = json.load(file)

usd = wallet.get("usd")
ntndo = 10
prixN = 10

while True:
    choix1 = input("que veux tu faire\n1. menu d'achat\n2. regarder les prix\n")
    
    if choix1 == "1":
        os.system("cls")
        choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
        if choix2 == "1":
            acht = input(f"que veux tu acheter ?\n1. Nintendo | prix: {ntndo}\n")
            if acht == "1":
                nombreA = input("combient en veux tu ?\n")
                nombreA = int(nombreA)
                ntndo = int(ntndo)
                prixT =  ntndo*nombreA
                prixT = str(prixT)
                if usd > prixT:
                    wallet["ntndo"] = nombreA
                    print(f"vous avez bien acheter {nombreA} d'action Nintendo pour le prix de {prixT}")
                    usd = int(usd)
                    prixT = int(prixT)
                    usd = usd - prixT
                else:
                    print("vous avez pas assez")
        if choix2 == "2":
            vndr = input(f"que veut tu vendre ?\n1. Nintendo | prix: {ntndo}\n")
            if vndr == "1":
                if wallet.__contains__("ntndo") == True:
                    nmbrVndr = input("commbien veut tu en vendre\n")
                    nmbrVndr = int(nmbrVndr)
                    if wallet.get("ntndo") >= nmbrVndr:
                        wallet["ntndo"] = wallet.get("ntndo") - nmbrVndr
                        tmp = nmbrVndr * ntndo
                        usd = usd + tmp
                        print(f"vous avez bien vendue {nmbrVndr} pour le prix de {tmp}")

    if choix1 == "2":
        for i in range(5):
            os.system("cls")
            prixN = ntndo
            ntndo = prixN + random.randint(-250, 250)

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