"""
import math
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hip = math.hypot(co, ca)
print("A hipotenusa é => {:.2f}".format(hip)) */
"""

# como é apenas um comando, para economizar
# dá pra utilizar apenas o hypot sem importar todo o math

from math import hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hip = hypot(co, ca)
print("A hipotenusa é => {:.2f}".format(hip))