import random
import time

bourse = 10

def affichageB(bourse, temp):
    if temp < bourse:
        print(f"le prix est a {temp} $ | actuellement -")
    if temp > bourse:
        print(f"le prix est a {temp} $ | actuellement +")

def calculB(bourse, temp):
    temp = bourse + random.randint(-15, 50)
    if temp < -50:
        bourse = bourse + random.randint(34, 1864)
    if temp > 15000:
        temp = bourse - random.randint(34, 1864)

while True:
    temp = bourse + random.randint(-15, 50)
    affichageB(bourse, temp)
    calculB(bourse, temp)
    bourse = temp
    time.sleep(0.5)