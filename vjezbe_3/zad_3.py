import math
import numpy as np


tocke=[2,4,6,9,10,36,32,12,8,1]

aritmeticka_sredina=sum(tocke)/len(tocke)

#standardna derivacija

brojnik_jed=[(el - aritmeticka_sredina)**2 for el in tocke]
suma_brojnik=sum(brojnik_jed)

standardna_derivacija=(suma_brojnik/len(tocke))**0.5

print(aritmeticka_sredina)
print(standardna_derivacija)
