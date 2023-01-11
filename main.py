 # # # Block module
#
import time
import os
from saveLoad import *
from acht import *
from vndr import *
from marque import *
#
 # # # Block module

 # # # Start Block
#
loadDB(wallet, price)

ntndo = price.get("ntndo")
apl = price.get("apl")
chnl = price.get("chnl")

usd = wallet.get("usd")
#
 # # # Start Block


 # # # Block fontion
#
# Block fonction menu d'achat vente
def menuA():
    os.system("cls")
    choix2 = input("que veut tu faire\n1. acheter\n2. vendre\n3. ton compte\n")
    if choix2 == "1":
        acheter(ntndo, apl, chnl, usd)
        
    if choix2 == "2":
        vendre(ntndo, apl, chnl, usd)

    if choix2 == "3":
        compte()

def compte():
    os.system("cls")
    print("dollars sur le compte: " + str(wallet.get("usd")))
    print("vous possedez:")
    print("Nintendo: " + str(wallet.get("ntndo")))
    print("Apple: " + str(wallet.get("apl")))
    print("Channel: " + str(wallet.get("chnl")))
    time.sleep(1.5)
    os.system("cls")
# Fin block fonction menu d'achat vente

# Block fonction prix
def prxC():
    for _ in range(5):
        os.system("cls")
        nintendo(ntndo)
        apple(apl)
        channel(chnl)
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
        prxC()
    
    time.sleep(1)
    saveDB(wallet, price)
#
 # # # Block boucle