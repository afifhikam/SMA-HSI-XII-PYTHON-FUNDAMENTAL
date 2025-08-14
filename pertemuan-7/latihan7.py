#no1


count = 10

while count > 0:
    print(count)
    count -= 1

print("Blastoff!")

#no2

angka_rahasia = 7  

while True:
    tebakan = int(input("Tebak angka (antara 1-10): "))  

    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break  
    else:
        print("Salah, coba lagi!")

print("Terima kasih sudah bermain!")

#no3

total = 0           
count = 0           

while True:
    data = input("Masukkan angka (ketik 'done' untuk selesai): ")

    if data.lower() == "done":
        break  

    try:
        angka = float(data)  
        total += angka       
        count += 1           
    except ValueError:
        print("Input tidak valid")
        continue  

if count > 0:
    rata_rata = total / count
    print(f"Total: {total}")
    print(f"Jumlah angka yang dimasukkan: {count}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang valid dimasukkan.")
