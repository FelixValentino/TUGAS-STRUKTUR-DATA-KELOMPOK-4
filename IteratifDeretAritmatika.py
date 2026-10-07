def deretAritmatika(a,b,n):
    hasil  = 0
    for i in range(n):
        hasil += a
        a += b
        
    print(hasil)

print("Deret Aritmatika")
deretAritmatika(5,1,10)