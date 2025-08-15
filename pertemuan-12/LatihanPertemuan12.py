#soal 1

with open("log_kegiatan.txt", "a") as file:
    
    kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
    
    file.write(kegiatan + "\n")
print("Kegiatan berhasil ditambahkan ke log.")

#soal 2

with open("sumber.txt", "r") as file_sumber:
    isi = file_sumber.read()  
with open("salinan.txt", "w") as file_salinan:
    file_salinan.write(isi)  
print("File berhasil disalin dari sumber.txt ke salinan.txt")

#soal 3
import os

nama_file = input("Masukkan nama file yang ingin dihapus: ")

if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ")
    if konfirmasi.lower() == "y":
        os.remove(nama_file)
        print(f"File '{nama_file}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")