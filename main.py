import random
import time

bourse = 10

def coursBourse(bourse):
    print(f"Le prix est de {bourse} $")
    time.sleep(0.5)
    bourse = bourse + random.randint(-10, 10)
    if bourse < -50:
        bourse = bourse + random.randint(34, 186)

while True:
    coursBourse(bourse)