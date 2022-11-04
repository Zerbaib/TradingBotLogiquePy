import time
import os
from saveLoad import *

def acheter(ntndo, apl, chnl, usd):
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