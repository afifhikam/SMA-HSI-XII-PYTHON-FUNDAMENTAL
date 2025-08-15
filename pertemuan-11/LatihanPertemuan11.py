#Soal 1

nama_file = input("Masukkan nama file: ")

try:
    with open(nama_file, 'r') as file:
        for baris in file:
            print(baris.upper().strip())
except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")

#Soal 2

nama_file = input("Masukkan nama file:")

try:
    with open(nama_file, 'r') as file:
        total = 0.0
        jumlah = 0

        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:"):
                angka = float(baris.strip().split(":")[1])
                total += angka
                jumlah += 1

        if jumlah > 0:
            rata_rata = total / jumlah
            print("Rata-rata Spam Confidence:", rata_rata)
        else:
            print("Tidak ada baris yang cocok.")

except FileNotFoundError:
    print("File tidak ditemukan.")
except Exception as e:
    print("Terjadi kesalahan:", e)


#Soal 3

nama_file = input("Masukkan nama file: ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                print(baris.upper().strip())
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")