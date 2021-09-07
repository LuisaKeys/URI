a = input().split()

numero_1 = int (a[0])
numero_2 = int (a[1])
numero_3 = int (a[2])

maior = numero_1

if numero_1 > numero_2 and numero_1 > numero_3: 
  maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
elif numero_3 > numero_1 and numero_3 > numero_1:  
  maior = numero_3
  
print ('{} eh o maior'.format(maior))
