import os
import time
from saveLoad import *

loadDB(wallet, price)

def vendre(ntndo, apl, chnl, usd):
    loadDB(wallet, price)
    vndr = input(f"que veut tu vendre ?\n1. Nintendo | prix: " + str(price.get("ntndo")) + "\n2. Apple | prix: " + str(price.get("apl")) + "\n3. Channel | prix " + str(price.get("chnl")) + "\n")
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
    saveDB(wallet, price)
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
    saveDB(wallet, price)
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
    saveDB(wallet, price)