import random
import time

bourse = 10

while True:
    prix = bourse
    bourse = prix + random.randint(-25, 250)

    if bourse != prix:
        if bourse < prix:
            print(f"le prix est a {bourse} $ | actuellement -")
        if bourse > prix:
            print(f"le prix est a {bourse} $ | actuellement +")
    else:
        print(f"le prix est a {bourse} $ | actuellement =")
    
    time.sleep(1)