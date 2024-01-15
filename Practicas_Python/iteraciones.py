n = 25
i = 1
while i * i < n:
    if n % i == 0:
        print (i)
        print (n // i)
    i = i + 1
if n % i == 0:
    print()