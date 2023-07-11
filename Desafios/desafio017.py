""""
caop= float(input('Comprimento do cateto oposto:'))
caad = float(input('Comprimento do cateto adjacente:'))
hip = (caop ** 2 + caad ** 2) ** 1/2
print('A hipotenusa vai medir {:.2f}'.format(hip))
"""

import math 
caop = float(input('Comprimento do cateto oposto:'))
caad = float(input('Comprimento do cateto adjacente:'))
hip = math.hypot(caop,caad)
print('A hipotenusa vai medir {:.2f}'.format(hip))
