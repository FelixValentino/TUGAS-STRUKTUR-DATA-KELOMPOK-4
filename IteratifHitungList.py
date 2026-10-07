def hitungList(listAngka):
    hasil = 0
    for i in range(len(listAngka)):
        hasil = hasil + listAngka[i]
    print(hasil)

angka = [1, 2, 3, 4, 5]
print("Hitung List")
hitungList(angka)