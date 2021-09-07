import math
entrada_1 = input().split()
entrada_2 = input().split()

x1 = float (entrada_1[0])
y1 = float (entrada_1[1])

x2 = float (entrada_2[0])
y2 = float (entrada_2[1])

s = (x2 - x1)**2
s1 = (y2 - y1)**2
total = s + s1
distancia = math.sqrt (total)
print ('{:.4f}'.format(distancia))
