import json

with open('wallet.txt', 'r') as file:
    wallet = json.load(file)
with open('price.txt','r') as file:
    price = json.load(file)

def loadDB(wallet, price):
    with open('wallet.txt', 'r') as file:
        wallet = json.load(file)
    with open('price.txt','r') as file:
        price = json.load(file)

def saveDB(wallet, price):
    with open('wallet.txt', 'w') as file:
        json.dump(wallet, file)
    with open('price.txt', 'w') as file:
        json.dump(price, file)