# Pertemuan 12 — Function (Membuat dan Menggunakan Function)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Sapaan Robot

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep Function.
- Memahami manfaat Function dalam pemrograman.
- Membuat Function menggunakan `def`.
- Memanggil Function.
- Menggunakan Function untuk mengurangi penulisan kode yang berulang.
- Membuat program Sapaan Robot menggunakan Function.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Nested Loop
- Baris dan Kolom
- end=""
- Membuat berbagai pola

Hari ini kita akan belajar bagaimana **mengelompokkan kode** agar program menjadi lebih rapi dan mudah digunakan kembali.

---

# Apa itu Function?

Function adalah **sekumpulan kode** yang memiliki tugas tertentu dan dapat digunakan berulang kali.

Bayangkan Function seperti sebuah mesin.

```
Tombol Ditekan

↓

Mesin Bekerja

↓

Hasil Keluar
```

Kita cukup memanggil mesin tersebut setiap kali dibutuhkan.

---

# Kenapa Menggunakan Function?

Bayangkan kita ingin menampilkan sapaan berkali-kali.

Tanpa Function

```python
print("Halo!")
print("Selamat Datang!")
print()

print("Halo!")
print("Selamat Datang!")
print()

print("Halo!")
print("Selamat Datang!")
```

Kode menjadi panjang.

---

Dengan Function

```python
def sapa():

    print("Halo!")
    print("Selamat Datang!")

sapa()
sapa()
sapa()
```

Kode menjadi lebih pendek dan mudah dibaca.

---

# Struktur Function

Function dibuat menggunakan kata kunci

```python
def
```

Bentuk umum

```python
def nama_function():

    perintah
```

---

# Membuat Function

Contoh

```python
def halo():

    print("Halo Dunia")
```

Program belum menampilkan apa pun.

Mengapa?

Karena Function baru dibuat, tetapi belum dipanggil.

---

# Memanggil Function

Untuk menjalankan Function.

Tuliskan nama Function diikuti tanda kurung.

```python
halo()
```

Program

```python
def halo():

    print("Halo Dunia")

halo()
```

Output

```
Halo Dunia
```

---

# Memanggil Function Berkali-kali

```python
def salam():

    print("Selamat Belajar Python!")

salam()
salam()
salam()
```

Output

```
Selamat Belajar Python!

Selamat Belajar Python!

Selamat Belajar Python!
```

---

# Nama Function

Gunakan nama yang mudah dipahami.

Contoh

```python
def tampilkan_menu():
```

```python
def hitung_total():
```

```python
def cetak_struk():
```

Hindari nama seperti

```python
def a():
```

karena sulit dipahami.

---

# Function Tidak Mengembalikan Nilai

Function sederhana hanya menjalankan perintah.

Contoh

```python
def garis():

    print("===================")

garis()
```

Output

```
===================
```

---

# Menggunakan Beberapa Function

Kita dapat membuat lebih dari satu Function.

```python
def judul():

    print("TOKO BUKU")

def garis():

    print("===================")

judul()
garis()
```

Output

```
TOKO BUKU
===================
```

---

# Function dan Input

Function juga bisa menggunakan variable yang dibuat di luar Function.

```python
nama = input("Nama : ")

def sapa():

    print("Halo", nama)

sapa()
```

Output

```
Halo Sandy
```

---

# Diagram Function

```
Program

↓

Memanggil Function

↓

Function Berjalan

↓

Perintah Dieksekusi

↓

Kembali ke Program
```

---

# Contoh Program

```python
def salam():

    print("====================")
    print("Selamat Datang")
    print("====================")

salam()
```

Output

```
====================
Selamat Datang
====================
```

---

# Menggunakan Function Berkali-kali

```python
def robot():

    print("Halo, Saya Robot!")

robot()
robot()
robot()
```

Output

```
Halo, Saya Robot!

Halo, Saya Robot!

Halo, Saya Robot!
```

---

# Project Hari Ini

## Sapaan Robot

Buat sebuah Function bernama

```python
robot()
```

Isi Function

```
Halo!

Nama saya Robo.

Senang bertemu denganmu.

Selamat belajar Python!
```

Kemudian panggil Function tersebut sebanyak **3 kali**.

Contoh Output

```
Halo!

Nama saya Robo.

Senang bertemu denganmu.

Selamat belajar Python!

-------------------------

Halo!

Nama saya Robo.

Senang bertemu denganmu.

Selamat belajar Python!

-------------------------

Halo!

Nama saya Robo.

Senang bertemu denganmu.

Selamat belajar Python!
```

---

# Challenge 1

Buat Function

```python
garis()
```

yang menghasilkan

```
========================
```

Gunakan Function tersebut setiap kali ingin membuat garis.

---

# Challenge 2

Buat Function

```python
judul()
```

yang menghasilkan

```
========================
ROBOT INFORMATION
========================
```

Kemudian panggil sebelum Function robot dijalankan.

---

# Challenge 3

Buat tiga Function berbeda.

```python
def salam():
```

```python
def perkenalan():
```

```python
def penutup():
```

Lalu panggil secara berurutan sehingga menghasilkan percakapan robot yang lengkap.

---

# Mini Challenge

Buat salah satu program berikut menggunakan beberapa Function.

- Mesin ATM
- Mesin Kasir
- Login Game
- Biodata
- Menu Restoran
- Informasi Sekolah

Minimal memiliki **3 Function** yang berbeda.

---

# Tips

✔ Berikan nama Function yang sesuai dengan tugasnya.

✔ Gunakan Function untuk kode yang sering digunakan.

✔ Pisahkan program menjadi beberapa bagian kecil agar lebih mudah dibaca.

✔ Jangan lupa memanggil Function setelah dibuat.

---

# Kesalahan yang Sering Terjadi

❌ Lupa memanggil Function.

Salah

```python
def halo():

    print("Halo")
```

Program tidak menghasilkan output.

Benar

```python
halo()
```

---

❌ Lupa tanda kurung.

Salah

```python
halo
```

Benar

```python
halo()
```

---

❌ Salah indentasi.

Salah

```python
def halo():
print("Halo")
```

Benar

```python
def halo():
    print("Halo")
```

---

❌ Memberi nama Function dengan angka di awal.

Salah

```python
def 1halo():
```

Benar

```python
def halo1():
```

---

# Ringkasan

Hari ini kita telah belajar:

✅ Apa itu Function

✅ Manfaat Function

✅ Keyword `def`

✅ Membuat Function

✅ Memanggil Function

✅ Menggunakan beberapa Function

✅ Mengurangi kode yang berulang

✅ Membuat Program Sapaan Robot

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Parameter
- Argument
- Return Value
- Mengirim data ke Function
- Project: Menghitung Luas Persegi Panjang
