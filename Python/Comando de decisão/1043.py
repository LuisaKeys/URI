A = input().split()

a = float (A[0])
b = float (A[1])
c = float (A[2])
per = a + b + c
if a>=b+c or b>=c+a or c>=a+b:
 ar = (a + b)*c/2
 print ('Area = {:.1f}'.format(ar))
else:
  print ('Perimetro = {:.1f}'.format(per))
