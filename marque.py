import random
from saveLoad import *

loadDB(wallet, price)

def nintendo(ntndo):
    prixN = ntndo
    ntndo = prixN + random.randint(-50, 100)
    if ntndo < 5:
        ntndo = 5
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;31;40m-\033[0m")
    elif ntndo == prixN:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;32;40m=\033[0m")
    elif ntndo < prixN:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;31;40m-\033[0m")
    else:
        print(f"le prix de Nintendo est a {ntndo} $ | actuellement \033[1;32;40m+\033[0m")
    price["ntndo"] = ntndo
    saveDB(wallet, price)

def apple(apl):
    prixA = apl
    apl = prixA + random.randint(-30, 200)
    if apl < 15:
        apl = 15
        print(f"le prix de Apple est a {apl} $ | actuellement \033[1;31;40m-\033[0m")
    elif apl == prixA:
        print(f"le prix de Apple est a {apl} $ | actuellement \033[1;32;40m=\033[0m")
    elif apl < prixA:
        print(f"le prix de Apple est a {apl} $ | actuellement \033[1;31;40m-\033[0m")
    else:
        print(f"le prix de Apple est a {apl} $ | actuellement \033[1;32;40m+\033[0m")
    price["apl"] = apl
    saveDB(wallet, price)

def channel(chnl):
    prixC = chnl
    chnl = prixC + random.randint(-20, 300)
    if chnl < 35:
        chnl = 35
        print(f"le prix de Nintendo est a {chnl} $ | actuellement \033[1;31;40m-\033[0m")
    elif chnl == prixC:
        print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;32;40m=\033[0m")
    elif chnl < prixC:
        print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;31;40m-\033[0m")
    else:
        print(f"le prix de Channel est a {chnl} $ | actuellement \033[1;32;40m+\033[0m")
    price["chnl"] = chnl
    saveDB(wallet, price)