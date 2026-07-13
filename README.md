# Pertemuan 9 — Looping (While Loop & For Loop)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Password Checker & Tabel Perkalian (Bagian 1)

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep perulangan (Looping).
- Mengetahui mengapa Loop diperlukan.
- Menggunakan `while` dan `for`.
- Menggunakan fungsi `range()`.
- Memahami Infinite Loop.
- Membuat program Password Checker sederhana.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- IF
- ELSE
- ELIF
- Nested IF

Hari ini kita akan belajar bagaimana membuat komputer **mengulang pekerjaan secara otomatis**.

---

# Apa itu Looping?

Looping adalah proses mengulang suatu perintah beberapa kali.

Tanpa Loop kita harus menulis kode berulang-ulang.

Contoh.

Tanpa Loop

```python
print("Halo")
print("Halo")
print("Halo")
print("Halo")
print("Halo")
```

Dengan Loop

```python
for i in range(5):
    print("Halo")
```

Hasilnya sama, tetapi kodenya jauh lebih singkat.

---

# Kenapa Menggunakan Loop?

Loop digunakan ketika pekerjaan dilakukan berulang.

Contohnya:

- Menghitung angka
- Menampilkan daftar
- Memeriksa data
- Membuat tabel
- Meminta input berulang
- Game

---

# Jenis Loop pada Python

Python memiliki dua jenis Loop utama.

- While Loop
- For Loop

---

# While Loop

While digunakan ketika kita belum tahu pasti berapa kali perulangan dilakukan.

Struktur

```python
while kondisi:
    perintah
```

Selama kondisi bernilai **True**, program akan terus mengulang.

---

# Contoh While

```python
angka = 1

while angka <= 5:
    print(angka)
    angka += 1
```

Output

```
1
2
3
4
5
```

---

# Bagaimana While Bekerja?

```
angka = 1

↓

Apakah angka <= 5 ?

↓

Ya

↓

Cetak angka

↓

Tambah 1

↓

Kembali ke kondisi
```

Program berhenti ketika kondisi bernilai False.

---

# Counter

Counter adalah variable yang menghitung jumlah perulangan.

Contoh

```python
counter = 1

while counter <= 3:
    print(counter)
    counter += 1
```

---

# Infinite Loop

Infinite Loop adalah perulangan yang tidak pernah berhenti.

Contoh

```python
while True:
    print("Halo")
```

Program akan berjalan terus hingga dihentikan.

---

# Kesalahan Umum While

```python
angka = 1

while angka <= 5:
    print(angka)
```

Program akan berjalan selamanya karena nilai `angka` tidak pernah berubah.

Harus ditambahkan.

```python
angka += 1
```

---

# For Loop

For digunakan ketika jumlah perulangan sudah diketahui.

Contoh

```python
for i in range(5):
    print("Python")
```

Output

```
Python
Python
Python
Python
Python
```

---

# Mengenal range()

`range()` menghasilkan urutan angka.

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

# range(start, stop)

```python
for i in range(1,6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

# range(start, stop, step)

```python
for i in range(2,11,2):
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

---

# While vs For

## While

Digunakan jika jumlah perulangan belum pasti.

Contoh:

- Login
- Password
- Menu Program

---

## For

Digunakan jika jumlah perulangan sudah diketahui.

Contoh:

- Cetak angka 1-100
- Daftar siswa
- Tabel perkalian

---

# Contoh Program For

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

# Contoh Program While

```python
nilai = 1

while nilai <= 5:
    print("Belajar Python")
    nilai += 1
```

Output

```
Belajar Python
Belajar Python
Belajar Python
Belajar Python
Belajar Python
```

---

# Diagram Loop

```
Mulai

↓

Kondisi Benar?

↓

Ya

↓

Jalankan Program

↓

Kembali ke Kondisi

↓

Tidak

↓

Selesai
```

---

# Project Hari Ini

## Password Checker

Buat program yang meminta pengguna memasukkan password.

Aturan:

Password yang benar adalah

```
python123
```

Program akan terus meminta password sampai pengguna memasukkan password yang benar.

Contoh

```
Masukkan Password :
abc

Password Salah

Masukkan Password :
123

Password Salah

Masukkan Password :
python123

Login Berhasil
```

Gunakan **While Loop**.

---

# Challenge 1

Batasi percobaan login sebanyak **3 kali**.

Jika gagal.

Tampilkan

```
Akun Diblokir
```

---

# Challenge 2

Tambahkan username.

Program meminta:

- Username
- Password

Baru melakukan pengecekan login.

---

# Challenge 3

Setelah login berhasil.

Tampilkan

```
======================

Selamat Datang

======================
```

---

# Mini Challenge

Buat salah satu program berikut.

- Login Game
- Login ATM
- Login WiFi
- PIN Handphone
- Login Website

Gunakan **While Loop**.

---

# Kesalahan yang Sering Terjadi

❌ Lupa menambah counter.

Salah

```python
angka = 1

while angka <= 5:
    print(angka)
```

Benar

```python
angka += 1
```

---

❌ Salah menentukan range.

```python
range(5)
```

Dimulai dari angka **0**, bukan **1**.

Jika ingin mulai dari 1.

```python
range(1,6)
```

---

❌ Infinite Loop tanpa sengaja.

Selalu pastikan kondisi akhirnya dapat menjadi **False**.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Konsep Looping

✅ While Loop

✅ For Loop

✅ Fungsi `range()`

✅ Counter

✅ Infinite Loop

✅ Perbedaan While dan For

✅ Membuat Password Checker

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Menggunakan `for` untuk membuat pola angka
- Tabel Perkalian
- Latihan berbagai bentuk perulangan
- Kombinasi Loop dan Conditional
- Project: Tabel Perkalian
