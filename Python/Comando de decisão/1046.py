entrada = input().split()

hinicio = int (entrada[0])
hfinal = int (entrada[1])

horas = hfinal - hinicio

if(hinicio == hfinal):
 print('O JOGO DUROU 24 HORA(S)') 
elif(horas < 0):
  horas = 24 + horas
  print('O JOGO DUROU {} HORA(S)'.format(horas))
else:
  print('O JOGO DUROU {} HORA(S)'.format(horas))
