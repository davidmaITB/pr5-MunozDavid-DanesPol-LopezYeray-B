'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

Mitjana de nombre aleatoris
'''
import random

numeros = [random.randint(1, 50) for _ in range(100)]
numeros_parelles = numeros[1::2]
media_parelles = (sum(numeros_parelles) // len(numeros_parelles))
numeros_senars = numeros[::2]
media_senars = sum(numeros_senars) // len(numeros_senars)

print(numeros)
print("mitjana posicions parelles:",media_parelles)
print("mitjana posicions senars:",media_senars)
