import json

with open('wallet.json', 'r') as file:
    wallet = json.load(file)
with open('price.json','r') as file:
    price = json.load(file)

def loadDB(wallet, price):
    with open('wallet.json', 'r') as file:
        wallet = json.load(file)
    with open('price.json','r') as file:
        price = json.load(file)

def saveDB(wallet, price):
    with open('wallet.json', 'w') as file:
        json.dump(wallet, file)
    with open('price.json', 'w') as file:
        json.dump(price, file)