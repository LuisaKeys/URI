s = float (input(''))
if 400.00 >= s >= 0:
 r = 0.15
 salario1 = s*r + s
 rr = s*r
 print ('Novo salario: {:.2f}'.format(salario1))
 print ('Reajuste ganho: {:.2f}'.format(rr))
 print ('Em percentual: 15 %')
if 800.00 >= s >= 400.01:
 r = 0.12
 salario1 = s*r + s
 rr = s*r
 print ('Novo salario: {:.2f}'.format(salario1))
 print ('Reajuste ganho: {:.2f}'.format(rr))
 print ('Em percentual: 12 %')
if 1200.00 >= s >= 800.01:
 r = 0.10
 salario1 = s*r + s
 rr = s*r
 print ('Novo salario: {:.2f}'.format(salario1))
 print ('Reajuste ganho: {:.2f}'.format(rr))
 print ('Em percentual: 10 %')

if 2000.00 >= s >= 1200.01:
 r = 0.07
 salario1 = s*r + s
 rr = s*r
 print ('Novo salario: {:.2f}'.format(salario1))
 print ('Reajuste ganho: {:.2f}'.format(rr))
 print ('Em percentual: 7 %')
 
if s > 2000.00 :
 r = 0.04
 salario1 = s*r + s
 rr = s*r
 print ('Novo salario: {:.2f}'.format(salario1))
 print ('Reajuste ganho: {:.2f}'.format(rr))
 print ('Em percentual: 4 %')
