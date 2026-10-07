def deretAritmatika(a, b, n):
    if n == 0:
        return 0
    else:
        return a + deretAritmatika(a + b, b, n - 1)
    
print("Deret Aritmatika")
print(deretAritmatika(1, 1, 5))