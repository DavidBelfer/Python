#importamos yogi
import yogi

#asignamos n a introducción de valor
n = yogi.read(int)

#cálculo de horas, minutos y segundos
h = n // 3600  #calculo valor insertado para horas "entero"
n %= 3600 #resto de segundos del valor insertado
m = n // 60 #numero de mintuos
s = n % 60 #numero de segundos

#damos salida a los valores y resultados
print (h , m , s)