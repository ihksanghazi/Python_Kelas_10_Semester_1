# Pertemuan 10 — Looping Lanjutan (For Loop & Tabel Perkalian)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Tabel Perkalian

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami penggunaan `for` secara lebih mendalam.
- Menggunakan fungsi `range()` dengan berbagai parameter.
- Membuat tabel perkalian menggunakan perulangan.
- Menggabungkan input, operator, dan perulangan.
- Menghindari penulisan kode yang berulang (redundansi).

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- While Loop
- For Loop
- range()
- Counter
- Infinite Loop
- Password Checker

Hari ini kita akan menggunakan **For Loop** untuk membuat program yang lebih bermanfaat.

---

# Mengapa Menggunakan For Loop?

Bayangkan kita ingin membuat tabel perkalian angka 5.

Tanpa Loop

```python
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)
```

Terlalu panjang.

Dengan Loop

```python
for i in range(1,11):
    print("5 x", i, "=", 5 * i)
```

Lebih singkat dan mudah dipahami.

---

# Review range()

Bentuk pertama

```python
range(stop)
```

Contoh

```python
range(5)
```

Menghasilkan

```
0
1
2
3
4
```

---

Bentuk kedua

```python
range(start, stop)
```

Contoh

```python
range(1,6)
```

Menghasilkan

```
1
2
3
4
5
```

---

Bentuk ketiga

```python
range(start, stop, step)
```

Contoh

```python
range(2,11,2)
```

Menghasilkan

```
2
4
6
8
10
```

---

# Menampilkan Angka

```python
for i in range(1,11):
    print(i)
```

Output

```
1
2
3
4
5
6
7
8
9
10
```

---

# Menampilkan Bilangan Genap

```python
for i in range(2,21,2):
    print(i)
```

Output

```
2
4
6
8
10
12
14
16
18
20
```

---

# Menampilkan Bilangan Ganjil

```python
for i in range(1,20,2):
    print(i)
```

Output

```
1
3
5
7
9
11
13
15
17
19
```

---

# Menggunakan Input

Program dapat meminta angka terlebih dahulu.

```python
angka = int(input("Masukkan Angka : "))
```

Kemudian

```python
for i in range(1,11):
    print(angka * i)
```

---

# Membuat Tabel Perkalian

```python
angka = int(input("Masukkan Angka : "))

for i in range(1,11):
    print(f"{angka} x {i} = {angka * i}")
```

Output

```
Masukkan Angka : 7

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

---

# Menggunakan f-string

Contoh

```python
angka = 9

for i in range(1,11):
    print(f"{angka} x {i} = {angka*i}")
```

Output menjadi lebih rapi.

---

# Diagram Program

```
Mulai

↓

Input Angka

↓

Perulangan

1 sampai 10

↓

Hitung

Angka × i

↓

Tampilkan

↓

Selesai
```

---

# Menggunakan Operator di Dalam Loop

```python
for i in range(1,6):
    hasil = i * 10
    print(hasil)
```

Output

```
10
20
30
40
50
```

---

# Menggabungkan Loop dan IF

Kita juga bisa menggunakan IF di dalam Loop.

```python
for i in range(1,11):

    if i % 2 == 0:
        print(i)
```

Output

```
2
4
6
8
10
```

Program hanya menampilkan bilangan genap.

---

# Contoh Program Lengkap

```python
angka = int(input("Masukkan Angka : "))

print()
print("======================")
print("TABEL PERKALIAN")
print("======================")

for i in range(1,11):
    print(f"{angka} x {i} = {angka*i}")

print("======================")
```

---

# Project Hari Ini

## Tabel Perkalian

Buat program yang meminta pengguna memasukkan sebuah angka.

Kemudian tampilkan tabel perkalian dari angka tersebut mulai dari:

```
1

sampai

10
```

Contoh

```
=========================
TABEL PERKALIAN
=========================

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80

=========================
```

---

# Challenge 1

Biarkan pengguna menentukan batas perkalian.

Input

```
Angka : 5

Sampai : 20
```

Output

```
5 x 1 = 5

...

5 x 20 = 100
```

---

# Challenge 2

Tambahkan keterangan.

Jika hasil perkalian lebih dari 50.

Tampilkan

```
Besar
```

Jika tidak.

Tampilkan

```
Kecil
```

Contoh

```
5 x 9 = 45 → Kecil

5 x 10 = 50 → Kecil

5 x 11 = 55 → Besar
```

---

# Challenge 3

Hitung jumlah seluruh hasil perkalian.

Contoh

```
5 x 1 = 5

...

5 x 10 = 50

-------------------

Total = 275
```

Petunjuk

Gunakan variable

```python
total = 0
```

Kemudian tambahkan setiap hasil perkalian ke dalam variable tersebut.

---

# Mini Challenge

Buat salah satu program berikut menggunakan **For Loop**.

- Tabel Pembagian
- Tabel Penjumlahan
- Tabel Pengurangan
- Konversi Meter ke Centimeter
- Konversi Celsius ke Fahrenheit
- Daftar Nomor Antrian

Gunakan minimal **1 input** dan **1 perulangan**.

---

# Tips

✔ Gunakan `range(1,11)` jika ingin menghitung dari 1 sampai 10.

✔ Gunakan **f-string** agar output lebih mudah dibaca.

✔ Simpan hasil perhitungan ke dalam variable jika akan digunakan kembali.

✔ Hindari menulis kode yang sama berulang-ulang.

---

# Kesalahan yang Sering Terjadi

❌ Salah menentukan batas `range()`.

```python
range(10)
```

Menghasilkan

```
0 sampai 9
```

Jika ingin

```
1 sampai 10
```

Gunakan

```python
range(1,11)
```

---

❌ Lupa mengubah input menjadi Integer.

Salah

```python
angka = input()
```

Benar

```python
angka = int(input())
```

---

❌ Salah menggunakan operator perkalian.

Salah

```python
angka + i
```

Padahal yang diinginkan adalah

```python
angka * i
```

---

❌ Salah menulis f-string.

Salah

```python
print("{angka}")
```

Benar

```python
print(f"{angka}")
```

---

# Ringkasan

Hari ini kita telah belajar:

✅ For Loop

✅ range()

✅ Input pada Loop

✅ Membuat Tabel Perkalian

✅ Menggabungkan Loop dan IF

✅ Menggunakan Operator dalam Loop

✅ Mengurangi penulisan kode yang berulang

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Nested Loop
- Loop di dalam Loop
- Membuat berbagai pola (Pattern)
- Menggunakan beberapa perulangan sekaligus
- Project: Membuat Pola
