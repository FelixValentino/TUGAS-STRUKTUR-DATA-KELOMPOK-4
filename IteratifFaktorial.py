def faktorial(n):
    
    hasil = 1
    temp = [1,2,3,4,5]
    for i in temp:
        hasil = hasil * n
        n -= 1
    print(hasil)
    
    
    hasil = 1
    temp = 0
    while temp < 5:
        hasil *= n
        n -= 1
        temp += 1
    print(hasil)
    

print("Faktorial")
faktorial(5)