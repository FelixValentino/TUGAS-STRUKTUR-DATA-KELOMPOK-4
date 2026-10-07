import os

def hitung_dan_tampilkan_folder(path_direktori):
    total_folder = 0
    try:
        daftar_item = os.listdir(path_direktori)
        
        for item in daftar_item:
            path_lengkap = os.path.join(path_direktori, item)
            
            # Jika berupa folder/direktori
            if os.path.isdir(path_lengkap):
                # 1. Cetak nama atau lokasi folder yang ditemukan
                print(f"Folder ditemukan: {path_lengkap}")
                
                # 2. Tambah hitungan (+1) dan lakukan rekursif ke dalamnya
                total_folder += 1 + hitung_dan_tampilkan_folder(path_lengkap)
                
    except PermissionError:
        pass
        
    return total_folder

# Lokasi folder Anda
lokasi_folder = r"C:\Users\hsjsb\OneDrive\Dokumen\Semester 3 - Struktur Data\Tugas Kelompok"

print("--- Daftar Subfolder ---")
jumlah_folder = hitung_dan_tampilkan_folder(lokasi_folder)
print("------------------------")
print(f"Total subfolder: {jumlah_folder}")
