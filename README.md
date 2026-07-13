# Pertemuan 4 — String Formatting (Membuat Output Lebih Rapi)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Digital ID Card

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami apa itu String Formatting.
- Menggabungkan teks dan variable dengan beberapa cara.
- Menggunakan operator koma (,), operator (+), method `.format()`, dan **f-string**.
- Memilih cara formatting yang paling tepat.
- Membuat tampilan output yang lebih rapi.
- Membuat program Digital ID Card.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- input()
- Variable
- Integer
- Float
- IPO
- Program Interaktif

Hari ini kita akan belajar bagaimana menampilkan data dengan lebih rapi.

---

# Apa itu String Formatting?

String Formatting adalah cara menyusun teks agar informasi yang ditampilkan menjadi lebih jelas, rapi, dan mudah dibaca.

Contoh yang kurang rapi:

```
Sandy23JakartaProgrammer
```

Lebih baik

```
Nama   : Sandy
Umur   : 23
Kota   : Jakarta
Profesi: Programmer
```

---

# Cara 1 — Menggunakan Tanda Koma (,)

Python dapat menampilkan beberapa data sekaligus.

```python
nama = "Sandy"
umur = 23

print("Nama :", nama)
print("Umur :", umur)
```

Output

```
Nama : Sandy
Umur : 23
```

Ini adalah cara yang paling mudah.

---

# Cara 2 — Menggunakan Operator (+)

String juga bisa digabungkan menggunakan tanda tambah.

```python
nama = "Sandy"

print("Halo " + nama)
```

Output

```
Halo Sandy
```

---

# Kenapa Bisa Error?

Perhatikan contoh berikut.

```python
umur = 23

print("Umur saya " + umur)
```

Output

```
TypeError
```

Karena Python tidak bisa menggabungkan String dengan Integer secara langsung.

---

# Mengubah Integer Menjadi String

Gunakan fungsi

```python
str()
```

Contoh

```python
umur = 23

print("Umur saya " + str(umur))
```

Output

```
Umur saya 23
```

---

# Cara 3 — Menggunakan format()

Python menyediakan method

```python
format()
```

Contoh

```python
nama = "Sandy"
umur = 23

print("Nama saya {} dan umur saya {} tahun".format(nama, umur))
```

Output

```
Nama saya Sandy dan umur saya 23 tahun
```

Tanda

```
{}
```

akan diganti sesuai urutan data.

---

# Menggunakan Banyak Placeholder

```python
nama = "Andi"
umur = 16
kelas = "10A"

print("{} berumur {} tahun dan berada di kelas {}".format(nama, umur, kelas))
```

Output

```
Andi berumur 16 tahun dan berada di kelas 10A
```

---

# Cara 4 — Menggunakan f-string

Mulai Python 3.6 terdapat cara yang lebih mudah.

Namanya

```
f-string
```

Contoh

```python
nama = "Sandy"
umur = 23

print(f"Nama saya {nama}")
print(f"Umur saya {umur}")
```

Output

```
Nama saya Sandy
Umur saya 23
```

---

# Kenapa f-string Lebih Baik?

Dengan f-string kita tidak perlu:

- memakai tanda +
- memakai format()

Kode menjadi lebih pendek dan mudah dibaca.

Contoh

```python
nama = "Sandy"
game = "Minecraft"

print(f"{nama} sedang bermain {game}")
```

Output

```
Sandy sedang bermain Minecraft
```

---

# Perbandingan Semua Cara

## Menggunakan Koma

```python
print("Nama :", nama)
```

---

## Menggunakan +

```python
print("Nama : " + nama)
```

---

## Menggunakan format()

```python
print("Nama : {}".format(nama))
```

---

## Menggunakan f-string

```python
print(f"Nama : {nama}")
```

---

Saat ini **f-string** adalah cara yang paling direkomendasikan karena lebih mudah dibaca.

---

# Karakter Khusus (Escape Character)

Kadang kita ingin membuat tampilan lebih rapi.

---

## Baris Baru

Gunakan

```python
\n
```

Contoh

```python
print("Python\nProgramming")
```

Output

```
Python
Programming
```

---

## Tab

Gunakan

```python
\t
```

Contoh

```python
print("Nama\t: Sandy")
print("Umur\t: 23")
```

Output

```
Nama    : Sandy
Umur    : 23
```

---

## Tanda Kutip

```python
print("Saya belajar \"Python\"")
```

Output

```
Saya belajar "Python"
```

---

# Membuat Tampilan Lebih Menarik

Contoh

```python
print("===================")
print("   DATA SISWA")
print("===================")
```

Output

```
===================
   DATA SISWA
===================
```

---

# Contoh Program

```python
nama = input("Nama : ")
umur = int(input("Umur : "))
kelas = input("Kelas : ")

print()
print("====================")
print("   DATA SISWA")
print("====================")
print(f"Nama  : {nama}")
print(f"Umur  : {umur}")
print(f"Kelas : {kelas}")
print("====================")
```

Output

```
====================
   DATA SISWA
====================
Nama  : Sandy
Umur  : 23
Kelas : X-A
====================
```

---

# Project Hari Ini

## Digital ID Card

Buat program yang meminta pengguna memasukkan:

- Nama
- Umur
- Sekolah
- Kelas
- Kota
- Hobi
- Cita-cita

Kemudian tampilkan dalam bentuk kartu identitas.

Contoh

```
================================
        STUDENT ID CARD
================================

Nama       : Sandy
Umur       : 23
Sekolah    : Jade School
Kelas      : X-A
Kota       : Jakarta
Hobi       : Coding
Cita-cita  : Software Engineer

================================
```

Gunakan **f-string** agar kode lebih mudah dibaca.

---

# Challenge 1

Tambahkan informasi berikut.

- Email
- Nomor HP
- Game Favorit
- Makanan Favorit
- Warna Favorit

---

# Challenge 2

Buat tampilan yang lebih menarik menggunakan:

- Garis pemisah
- Judul
- Tab (`\t`)
- Baris baru (`\n`)

Contoh

```
****************************************
          STUDENT PROFILE
****************************************

Nama          : Sandy
Sekolah       : Jade School
Kelas         : X-A
Game Favorit  : Minecraft
Hobi          : Coding
Cita-cita     : AI Engineer

****************************************
```

---

# Mini Challenge

Buat **ID Card** untuk salah satu karakter berikut:

- Superhero
- Karakter Anime
- Tokoh Game
- Karakter Roblox
- Karakter Minecraft

Gunakan minimal **8 informasi**.

---

# Kesalahan yang Sering Terjadi

❌ Lupa menambahkan huruf **f**

```python
print("{nama}")
```

Harusnya

```python
print(f"{nama}")
```

---

❌ Menggunakan operator + dengan Integer

```python
print("Umur : " + umur)
```

Harus diubah menjadi

```python
print("Umur : " + str(umur))
```

atau lebih baik

```python
print(f"Umur : {umur}")
```

---

❌ Placeholder format() tidak sesuai jumlah data

```python
print("{} {}".format(nama))
```

Jumlah `{}` harus sama dengan jumlah data yang dikirim.

---

# Ringkasan

Hari ini kita telah belajar:

✅ String Formatting

✅ Operator Koma (,)

✅ Operator (+)

✅ Konversi menggunakan `str()`

✅ Method `.format()`

✅ f-string

✅ Escape Character (`\n`, `\t`, `\"`)

✅ Membuat tampilan output lebih rapi

✅ Membuat Digital ID Card

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Library pada Python
- Import Module
- Library `random`
- Library `time`
- Library `os`
- Project: Dice Simulator
