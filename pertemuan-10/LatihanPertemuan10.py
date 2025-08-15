# soal 1

judul_input = input("Masukkan judul buku: ")

judul_bersih = judul_input.strip().title()

print("Judul yang distandarisasi:", judul_bersih)

# soal 2

email = input("Masukkan alamat email: ").strip()

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")

# soal 3

kalimat = input("Masukkan kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")

kalimat_disensor = kalimat.replace(kata_sensor, "***")

print("Kalimat setelah disensor:")
print(kalimat_disensor)

# soal 4

nama_organisasi = input("Masukkan nama organisasi: ")

kata_kata = nama_organisasi.strip().split()

huruf_pertama = [kata[0].upper() for kata in kata_kata]

akronim = ''.join(huruf_pertama)

print("Akronim:", akronim)

# soal 5
import re
judul = input("Masukkan judul artikel: ")

judul_kecil = judul.lower()

judul_slug = judul_kecil.replace(" ", "-")

slug_bersih = re.sub(r'[^a-z0-9\-]', '', judul_slug)

print("Slug URL:", slug_bersih)
