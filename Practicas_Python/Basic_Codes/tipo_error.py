# tipos de datos. No podremos realizar operaciones con integer y strings (pjemplo)

import yogi
n=yogi.read(int)
if n == 666:
    print (2 + 'tres')

#mientras no sea 666 dará OK pero en el momento que sea 666 dará error
#usar mypy error.py sirve para encontrar errores y obtener programas fiables antes de ejecutarlos


