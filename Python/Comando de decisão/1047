entrada = input().split()

i = int(entrada[0])
f = int(entrada[2])
mi = int(entrada[1])
mf = int(entrada[3])
h = 24

if (f == i) and (mf == mi):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
 if f > i:
   h = f - i
 if i > f:
   h = (24 - i) + f
 if mf > mi:
   m = mf - mi
 if mi > mf:
   m = (60 - mi) + mf
   h -= 1
 if (i == f) and (mf > mi):
   h = 0
   m = mf - mi
 if (f > i) and (mi == mf):
   h = f - i 
   m = 0
 if (f < i) and (mi == mf):
   h = h 
   m = 0
 print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
