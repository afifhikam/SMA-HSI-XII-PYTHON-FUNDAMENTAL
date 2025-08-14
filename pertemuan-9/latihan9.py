# soal 1
s = "Belajar Python itu Menyenangkan"

print("Karakter pertama:", s[0])

print("Karakter terakhir:", s[-1])

print("Karakter spasi pertama:", s[7])

# soal 2
s = "Belajar Python itu Menyenangkan"

print("Substring 1:", s[8:14])

print("Substring 2:", s[20:])

print("Substring 3:", s[:7])

# soal 3

kata = input("Masukkan sebuah kata atau kalimat: ")

kata_terbalik = kata[::-1]

print("Kebalikannya:", kata_terbalik)

kata_bersih = kata.replace(" ", "").lower()
terbalik_bersih = kata_terbalik.replace(" ", "").lower()

if kata_bersih == terbalik_bersih:
    print("Ini adalah palindrom!")
else:
    print("Ini bukan palindrom.")

# soal 4
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

kode_rahasia = kalimat[::3]

print("Kode Rahasia:", kode_rahasia)

# soal 5
nama_salah = "dUDI sANTOSO"

huruf1 = "B"                 
sisa1 = nama_salah[1:4].lower()  
nama_depan = huruf1 + sisa1     

huruf2 = nama_salah[5].upper()  
sisa2 = nama_salah[6:].lower()  
nama_belakang = huruf2 + sisa2  

nama_benar = nama_depan + " " + nama_belakang

print("Nama yang benar:", nama_benar)