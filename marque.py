import json
import time
import os
import random

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

def nintendo(ntndo):
    prixN = ntndo
    ntndo = prixN + random.randint(-100, 100)
    if ntndo != prixN:
        if ntndo < prixN:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement =")
    price["ntndo"] = ntndo
def apple(apl):
    prixA = apl
    apl = prixA + random.randint(-100, 100)
    if apl != prixA:
        if apl < prixA:
            print(f"le prix de Apple est a {apl} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Apple est a {apl} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Apple est a {apl} $ | actuellement =")
    price["apl"] = apl
def channel(chnl):
    prixC = chnl
    chnl = prixA + random.randint(-100, 100)
    if chnl != prixC:
        if chnl < prixC:
            print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Channel est a {chnl} $ | actuellement =")
    price["chnl"] = chnl