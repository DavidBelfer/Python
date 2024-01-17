from yogi import read

def nombre_divisors (n: int) -> None:
    
    i=1 #asignación del valor i
    while i * i < n: #mientras un número multiplicado por otro sea menor a número insertado haz el bucle
        
        if n % i == 0: # si el resto del número insertado y la asignación es 0 , muestra la asignación
            print(i)
        i = i + 1 # vuelves a ejecutar sumando un valor más a la asignación
        
        if i * i == n: # si la asignación (i) multiplicada por (i) es igual a la variable
            print(i) # imprimes la asignación (i)
        
    while i > 1:
        
        if n % i == 0:
            print (n // i)
        i = i - 1

nombre_divisors(read (int))