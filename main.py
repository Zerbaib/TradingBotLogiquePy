 # # # Block module
#
import random
from socketserver import UDPServer
import time
import os
import json
from xml.dom.domreg import well_known_implementations
import AchVente
import marque
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
        AchVente.menuA1(ntndo, apl, chnl, usd)
        
    if choix2 == "2":
        AchVente.menuA2(ntndo, apl, chnl, usd)

    if choix2 == "3":
        AchVente.menuA3()
# Fin block fonction menu d'achat vente

# Block fonction prix
def prixCA():
    for i in range(5):
        os.system("cls")
        marque.nintendo(ntndo)
        marque.apple(apl)
        marque.channel(chnl)
        time.sleep(1)
        os.system("cls")
# Fin block fonction prix
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