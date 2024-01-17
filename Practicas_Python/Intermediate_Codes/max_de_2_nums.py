
import yogi #read
#Laboratorio - ejercicio para leer dos enteros
#x = int(input())
#y = int(input())


str(print ('Elige un número: '))
x = yogi.read(int)
str(print('Elige otro número: '))
y = yogi.read(int)

#comprobar cuál es el valor mayor
if x > y:
    str(print ('El número mayor es: ' ,x))
else:
    str(print ('El número mayor es: ' ,y))
  