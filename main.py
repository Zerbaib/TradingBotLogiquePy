import random
import time
import os
import json

ntndo = 10
prixN = 10

def saveW():
    with open('wallet.txt', 'w') as file:
        json.dump(wallet, file)

def startW():
    with open('wallet.txt', 'r') as file:
        wallet = json.load(file)

def bourse1(ntndo, prixN):
    prixN = ntndo
    ntndo = prixN + random.randint(-250, 250)

    if ntndo != prixN:
        if ntndo < prixN:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement -")
        else:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement +")
    else:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement =")

def achatVente(wallet, ntndo):
    os.system("cls")
    choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
    if choix2 == "1":
        acht = input(f"que veux tu acheter ?\n1. Nintendo | prix: {ntndo}")
        if acht == 1:
            nombreA = input("combient en veux tu ?")
            wallet[ntndo] = nombreA
            
startW()
while True:
    choix1 = input("que veux tu faire\n1. acheter\n2. regarder les prix\n")
    if choix1 == "1":
        achatVente(ntndo)
    if choix1 == "2":
        bourse1(ntndo, prixN)
    
    time.sleep(1)
    # os.system('cls')