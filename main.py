import random
import time

bourse = 10
prix = bourse

def affichageB(bourse, prix):
    if bourse == prix:
        print(f"le prix est a {bourse} $ | actuellement =")
    if bourse < prix:
        print(f"le prix est a {bourse} $ | actuellement -")
    if bourse > prix:
        print(f"le prix est a {bourse} $ | actuellement +")

def calculB(bourse, prix):
    prix = bourse
    bourse = bourse + 10 #random.randint(-15, 50)
    print(bourse)
    print(prix)

while True:
    calculB(bourse, prix)

    affichageB(bourse, prix)    
    
    time.sleep(1)