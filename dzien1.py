x1 = 1
y1 = 1

x2 = 4
y2 = 5

x3 = 11
y3 = 5

import math
Odległosc = math.sqrt( (x2-x1)**2 + (y2-y1)**2 ) + math.sqrt( (x3-x2)**2 + (y3-y2)**2 )

paliwo = (Odległosc*20)/10

print(paliwo)

