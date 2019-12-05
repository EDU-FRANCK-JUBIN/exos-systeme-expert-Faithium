# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:54:38 2019

@author: ilias
"""

from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.load("""
    frog(X) <= croakes(X) & eatsFlies(X)
    canary(X) <= chirps(X) & signs(X)
    green(X) <= frog(X)
    yellow(X) <= canary(X)

    + croakes(anAnimal)
    + eatsFlies(anAnimal)   
    + signs(piou)    
""")

print(pyDatalog.ask('green(X)'))
print(pyDatalog.ask('frog(X)'))
print(pyDatalog.ask('signs(X)'))

pyDatalog.clear()

pyDatalog.create_terms('X, frog, canary, croakes, eatsFlies, chirps, signs, green, yellow')
frog(X) <= croakes(X) & eatsFlies(X)
canary(X) <= chirps(X) & signs(X)
green(X) <= frog(X)
yellow(X) <= canary(X)

+croakes('anAnimal')
+eatsFlies('anAnimal')   
+signs('piou')


print(pyDatalog.ask('green(X)'))
print(pyDatalog.ask('frog(X)'))
print(pyDatalog.ask('signs(X)'))