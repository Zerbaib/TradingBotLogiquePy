import random
from saveLoad import *

loadDB(wallet, price)

def nintendo(ntndo):
    prixN = ntndo
    ntndo = prixN + random.randint(-100, 100)
    if ntndo != prixN:
        if ntndo < prixN:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;32;40m=\033[0m")
    price["ntndo"] = ntndo
    saveDB(wallet, price)

def apple(apl):
    prixA = apl
    apl = prixA + random.randint(-100, 100)
    if apl != prixA:
        if apl < prixA:
            print(f"le prix de Apple est a {apl} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Apple est a {apl} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Apple est a {apl} $ | actuellement \033[1;32;40m=\033[0m")
    price["apl"] = apl
    saveDB(wallet, price)

def channel(chnl):
    prixC = chnl
    chnl = prixC + random.randint(-100, 100)
    if chnl != prixC:
        if chnl < prixC:
            print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;31;40m-\033[0m")
        else:
            print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;32;40m+\033[0m")
    else:
        print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;32;40m=\033[0m")
    price["chnl"] = chnl
    saveDB(wallet, price)