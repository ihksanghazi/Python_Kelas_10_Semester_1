# Pertemuan 3 — Input, Variable & Konsep IPO (Program Interaktif)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Game Profile

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami fungsi `input()` pada Python.
- Mengambil data dari pengguna.
- Menyimpan hasil input ke dalam variable.
- Memahami kembali konsep IPO (Input → Process → Output).
- Membuat program profile interaktif.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Variable
- Aturan penamaan variable
- String
- Integer
- Float
- Boolean

Hari ini kita akan membuat program yang bisa **berinteraksi dengan pengguna.**

---

# Apa itu Program Interaktif?

Program interaktif adalah program yang dapat menerima masukan dari pengguna.

Contohnya:

- Login
- Registrasi akun
- Mesin ATM
- Game
- Formulir online

Program tidak hanya menampilkan informasi, tetapi juga menunggu pengguna memasukkan data.

---

# Mengenal Fungsi input()

Fungsi

```python
input()
```

digunakan untuk meminta data dari pengguna.

Contoh

```python
nama = input("Masukkan nama : ")
```

Program akan berhenti sementara hingga pengguna mengetik sesuatu.

Misalnya pengguna mengetik

```
Andi
```

Maka isi variable

```python
nama
```

adalah

```
Andi
```

---

# Menampilkan Hasil Input

Data yang dimasukkan pengguna dapat ditampilkan kembali.

```python
nama = input("Masukkan nama : ")

print(nama)
```

Output

```
Masukkan nama : Andi

Andi
```

---

# Input Selalu Menghasilkan String

Perhatikan contoh berikut.

```python
umur = input("Masukkan umur : ")

print(type(umur))
```

Walaupun pengguna mengetik

```
16
```

Output

```
<class 'str'>
```

Karena secara default `input()` selalu menghasilkan **String**.

---

# Mengubah String Menjadi Integer

Jika kita ingin menggunakan angka, kita harus mengubah tipe datanya.

Gunakan

```python
int()
```

Contoh

```python
umur = int(input("Masukkan umur : "))
```

Sekarang

```python
print(type(umur))
```

Output

```
<class 'int'>
```

---

# Mengubah Menjadi Float

Jika menggunakan angka desimal

```python
tinggi = float(input("Masukkan tinggi : "))
```

Contoh input

```
170.5
```

Output

```
170.5
```

---

# Mengambil Banyak Input

Kita dapat meminta beberapa data sekaligus.

```python
nama = input("Nama : ")
umur = int(input("Umur : "))
kota = input("Kota : ")
```

Program akan meminta data satu per satu.

---

# Menggabungkan Input dan Output

Contoh

```python
nama = input("Nama : ")

print("Halo", nama)
```

Jika pengguna mengetik

```
Sandy
```

Output

```
Halo Sandy
```

---

# Review Konsep IPO

Semua program memiliki tiga bagian.

## Input

Data yang dimasukkan pengguna.

Contoh

- Nama
- Umur
- Kota
- Email

↓

## Process

Program menyimpan dan mengolah data.

↓

## Output

Program menampilkan hasil kepada pengguna.

---

# IPO Pada Program Profile

Input

```
Nama
Umur
Game Favorit
Rank
```

↓

Process

Program menyimpan semua data ke dalam variable.

↓

Output

Program menampilkan profile pemain.

---

# Diagram IPO

```
+------------------+
|      INPUT       |
|------------------|
| Nama             |
| Umur             |
| Game Favorit     |
| Rank             |
+--------+---------+
         |
         v
+------------------+
|     PROCESS      |
|------------------|
| Simpan ke        |
| Variable         |
+--------+---------+
         |
         v
+------------------+
|      OUTPUT      |
|------------------|
| Menampilkan      |
| Profile Player   |
+------------------+
```

---

# Contoh Program

```python
nama = input("Nama Player : ")
umur = int(input("Umur : "))
game = input("Game Favorit : ")

print("===== PROFILE =====")
print("Nama :", nama)
print("Umur :", umur)
print("Game :", game)
```

Output

```
Nama Player : Sandy
Umur : 23
Game Favorit : Minecraft

===== PROFILE =====
Nama : Sandy
Umur : 23
Game : Minecraft
```

---

# Project Hari Ini

## Game Profile

Buat program yang meminta pengguna memasukkan data berikut:

- Nama Player
- Nickname
- Umur
- Game Favorit
- Rank
- Negara

Kemudian tampilkan hasilnya seperti berikut.

```
==========================
      PLAYER PROFILE
==========================

Nama        : Sandy
Nickname    : Zero
Umur        : 23
Game        : Minecraft
Rank        : Diamond
Negara      : Indonesia

==========================
```

---

# Challenge

Tambahkan informasi berikut.

- Level
- Total Win
- Total Match
- Senjata Favorit
- Hero Favorit

Kemudian tampilkan hasilnya agar lebih menarik.

Contoh

```
==========================
PLAYER PROFILE
==========================

Nama          : Sandy
Nickname      : Zero
Game          : Valorant
Rank          : Ascendant
Level         : 120
Total Win     : 540
Weapon        : Vandal

Selamat bermain!

==========================
```

---

# Mini Challenge

Buat profile untuk karakter game favorit kalian.

Contoh:

- Minecraft
- Roblox
- Mobile Legends
- Free Fire
- Valorant
- Genshin Impact

Gunakan kreativitas masing-masing.

---

# Kesalahan yang Sering Terjadi

❌ Lupa tanda kurung

```python
input
```

Harusnya

```python
input()
```

---

❌ Salah menulis nama variable

```python
Nama = input()

print(nama)
```

Python membedakan huruf besar dan kecil.

---

❌ Tidak mengubah angka menjadi Integer

```python
umur = input()
```

Jika ingin digunakan sebagai angka

```python
umur = int(input())
```

---

# Ringkasan

Hari ini kita telah belajar:

✅ Program interaktif

✅ Fungsi `input()`

✅ Input String

✅ Konversi menggunakan `int()`

✅ Konversi menggunakan `float()`

✅ Menggunakan banyak input

✅ Review konsep IPO

✅ Membuat Game Profile

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- String Formatting
- f-string
- `.format()`
- Escape Character
- Membuat output yang lebih rapi dan profesional
- Project: Digital ID Card
