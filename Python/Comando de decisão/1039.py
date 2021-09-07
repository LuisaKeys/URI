try:
 while True:
  import math 

  todos = str (input()).split()

  r1 = int (todos[0])
  x1 = int (todos[1])
  y1 = int (todos[2])

  r2 = int (todos[3])
  x2 = int (todos[4])
  y2 = int (todos[5])

  if r1 >= (math.hypot(x2 - x1, y2 - y1) + r2):
   print('RICO')

  else:
   print('MORTO')
except EOFError:
 exit()
