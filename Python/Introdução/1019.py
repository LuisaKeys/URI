total =int (input())

horas = total//3600
horas_em_minutos = horas * 3600
subtotal = total - horas_em_minutos

minutos = subtotal // 60
minutos_em_segundos = minutos * 60 

segundos = subtotal - minutos_em_segundos

print('{}:{}:{}'.format(horas, minutos, segundos))
