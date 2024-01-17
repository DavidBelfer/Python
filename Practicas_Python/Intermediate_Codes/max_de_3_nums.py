import yogi

#max de estos tres valore : 736 291 348
x = yogi.read(int)
y = yogi.read(int)
z = yogi.read(int)

if x >= y and x >= z:
    print (x)
elif y >= x and y >= z:
    print (y)
else:
    print(z)