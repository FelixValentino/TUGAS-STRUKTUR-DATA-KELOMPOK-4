def hitungList(listAngka):
    if not listAngka:
        return 0
    
    return listAngka[0] + hitungList(listAngka[1:])

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Hitung List")
print(hitungList(angka))