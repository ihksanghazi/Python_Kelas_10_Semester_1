# File: pertemuan_10.py
tinggi = int(input("Masukkan tinggi segitiga bintang: "))

print("\nHasil Pola Bintang:")
for baris in range(1, tinggi + 1):
    for kolom in range(baris):
        print("* ", end="")
    print()