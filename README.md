# Pertemuan 11 — Nested Loop (Loop di Dalam Loop)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Membuat Pola (Pattern)

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep Nested Loop.
- Mengetahui perbedaan Loop biasa dan Nested Loop.
- Menggunakan `for` di dalam `for`.
- Membuat berbagai pola menggunakan Nested Loop.
- Menganalisis hubungan antara baris dan kolom.
- Membuat pola sederhana menggunakan karakter.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- For Loop
- While Loop
- range()
- Tabel Perkalian

Hari ini kita akan belajar bagaimana membuat **perulangan di dalam perulangan**.

---

# Apa itu Nested Loop?

Nested Loop adalah **Loop yang berada di dalam Loop lainnya**.

Artinya, ketika Loop luar berjalan satu kali, Loop dalam akan berjalan hingga selesai.

Contohnya seperti kalender.

```
Minggu

↓

Senin
Selasa
Rabu
Kamis
Jumat
Sabtu
Minggu
```

Setiap minggu memiliki beberapa hari.

---

# Analogi Nested Loop

Bayangkan sebuah gedung sekolah.

```
Lantai 1

→ Ruang 1
→ Ruang 2
→ Ruang 3

Lantai 2

→ Ruang 1
→ Ruang 2
→ Ruang 3
```

Setiap lantai memiliki beberapa ruangan.

Loop luar mengulang lantai.

Loop dalam mengulang ruangan.

---

# Struktur Nested Loop

```python
for i in range(...):

    for j in range(...):

        print(...)
```

Loop luar mengatur jumlah **baris**.

Loop dalam mengatur jumlah **kolom**.

---

# Contoh Pertama

```python
for i in range(3):
    for j in range(3):
        print("*")
```

Output

```
*
*
*
*
*
*
*
*
*
```

Karena setiap `print()` berpindah ke baris baru.

---

# Menggunakan end=""

Agar hasil tetap pada baris yang sama gunakan

```python
end=""
```

Contoh

```python
for i in range(5):
    print("*", end="")
```

Output

```
*****
```

---

# Membuat Persegi

```python
for i in range(5):

    for j in range(5):
        print("*", end="")

    print()
```

Output

```
*****
*****
*****
*****
*****
```

Perhatikan

```python
print()
```

digunakan untuk berpindah ke baris berikutnya.

---

# Memahami Baris dan Kolom

```
Baris

↓

*****

*****

*****

↑

Kolom
```

Loop luar mengulang jumlah baris.

Loop dalam mengulang jumlah kolom.

---

# Menampilkan Angka

```python
for i in range(3):

    for j in range(5):
        print(j, end=" ")

    print()
```

Output

```
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
```

---

# Menggunakan Variable Loop

```python
for baris in range(3):

    for kolom in range(4):
        print("*", end=" ")

    print()
```

Menggunakan nama variable yang jelas membuat kode lebih mudah dipahami.

---

# Membuat Persegi Panjang

```python
for baris in range(4):

    for kolom in range(8):
        print("#", end=" ")

    print()
```

Output

```
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
```

---

# Menggunakan Input

Pengguna dapat menentukan ukuran pola.

```python
ukuran = int(input("Masukkan Ukuran : "))
```

Kemudian

```python
for i in range(ukuran):

    for j in range(ukuran):
        print("*", end="")

    print()
```

---

# Diagram Nested Loop

```
Loop Luar

↓

Baris 1

↓

Loop Dalam

↓

Kolom 1
Kolom 2
Kolom 3

↓

Selesai

↓

Baris 2

↓

Loop Dalam Lagi
```

---

# Contoh Program Lengkap

```python
ukuran = int(input("Masukkan Ukuran : "))

print()

for baris in range(ukuran):

    for kolom in range(ukuran):
        print("*", end=" ")

    print()
```

Output

```
Masukkan Ukuran : 5

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

# Project Hari Ini

## Membuat Pola

Buat program yang meminta pengguna memasukkan ukuran pola.

Misalnya

```
Ukuran : 6
```

Program menghasilkan

```
******
******
******
******
******
******
```

Gunakan **Nested Loop**.

---

# Challenge 1

Buat pola angka.

Contoh

```
11111
22222
33333
44444
55555
```

Petunjuk

Gunakan variable dari Loop luar.

---

# Challenge 2

Buat pola seperti berikut.

```
12345
12345
12345
12345
12345
```

Petunjuk

Gunakan variable dari Loop dalam.

---

# Challenge 3

Buat papan permainan sederhana.

Contoh

```
□ □ □ □ □

□ □ □ □ □

□ □ □ □ □

□ □ □ □ □

□ □ □ □ □
```

Gunakan karakter lain jika terminal tidak mendukung simbol kotak.

---

# Mini Challenge

Buat salah satu pola berikut.

Pola 1

```
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@
```

---

Pola 2

```
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
```

---

Pola 3

```
#####
#####
#####
#####
#####
```

Gunakan ukuran yang dimasukkan oleh pengguna.

---

# Tips

✔ Loop luar biasanya digunakan untuk **baris**.

✔ Loop dalam biasanya digunakan untuk **kolom**.

✔ Gunakan `end=""` agar karakter tetap berada pada baris yang sama.

✔ Gunakan `print()` kosong untuk pindah ke baris berikutnya.

✔ Berikan nama variable yang jelas seperti `baris` dan `kolom`.

---

# Kesalahan yang Sering Terjadi

❌ Lupa menggunakan `end=""`.

Salah

```python
print("*")
```

Output

```
*
*
*
*
*
```

Benar

```python
print("*", end="")
```

Output

```
*****
```

---

❌ Lupa `print()` setelah Loop dalam selesai.

Akibatnya semua karakter akan tercetak dalam satu baris panjang.

---

❌ Salah indentasi.

Salah

```python
for i in range(5):
for j in range(5):
    print("*")
```

Benar

```python
for i in range(5):
    for j in range(5):
        print("*", end="")

    print()
```

---

❌ Menggunakan ukuran yang salah.

Jika pengguna memasukkan ukuran.

```
5
```

Pastikan kedua Loop menggunakan ukuran tersebut.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Konsep Nested Loop

✅ Loop di dalam Loop

✅ Hubungan Baris dan Kolom

✅ `end=""`

✅ Membuat Pola

✅ Menggunakan Input pada Nested Loop

✅ Membuat papan sederhana menggunakan Nested Loop

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Function
- Keyword `def`
- Memanggil Function
- Parameter sederhana
- Manfaat Function untuk membuat kode lebih rapi
- Project: Sapaan Robot
