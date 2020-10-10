"""
Programa que calcula la probabilidad de que en una habitación
con al menos 23 personas cumplan el mismo día años
"""

import numpy as np

n=365
k=23

p=1

for k in np.arange(1,k):
    p=p*(1-k/n)

p=1-p

print(p)
