n=int(input())
par = 0
if n%2==1:
 n=n-1
 while par < n:
   par+=2
   print('{}^2 = {}'.format(par, par * par))
if n%2==0:
  while par<n:
   par+=2
   print('{}^2 = {}'.format(par, par * par))
