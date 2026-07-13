# Pertemuan 14 — Debugging (Mencari dan Memperbaiki Error)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Guessing Number (Aplikasi Kuis Interaktif)

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami apa itu Bug dan Debugging.
- Mengenal jenis-jenis Error pada Python.
- Membaca Error Message.
- Menemukan penyebab Error.
- Memperbaiki program yang mengalami Error.
- Membuat aplikasi Guessing Number sederhana.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Function
- Parameter
- Argument
- Return Value

Hari ini kita akan belajar keterampilan yang dimiliki semua programmer, yaitu **Debugging**.

---

# Apa itu Bug?

Bug adalah kesalahan pada program yang menyebabkan program:

- Tidak dapat dijalankan.
- Menghasilkan hasil yang salah.
- Berhenti secara tiba-tiba (Crash).

Contoh sederhana.

Kita ingin menghitung

```
10 + 5
```

Tetapi program malah menghasilkan

```
50
```

Berarti terdapat Bug pada program.

---

# Apa itu Debugging?

Debugging adalah proses mencari, memahami, dan memperbaiki Bug pada program.

Seorang programmer tidak hanya membuat program, tetapi juga harus mampu memperbaiki kesalahan yang muncul.

---

# Mengapa Debugging Penting?

Dalam dunia nyata, hampir semua programmer melakukan debugging setiap hari.

Karena:

- Tidak ada program yang langsung sempurna.
- Error adalah bagian dari proses belajar.
- Semakin cepat menemukan Bug, semakin cepat program selesai.

---

# Jenis-Jenis Error

Secara umum terdapat tiga jenis Error.

- Syntax Error
- Runtime Error
- Logical Error

---

# 1. Syntax Error

Syntax Error terjadi karena aturan penulisan Python tidak benar.

Contoh

```python
if 10 > 5
    print("Benar")
```

Output

```
SyntaxError
```

Penyebabnya karena lupa menambahkan tanda

```
:
```

Perbaikan

```python
if 10 > 5:
    print("Benar")
```

---

# 2. Runtime Error

Runtime Error muncul ketika program sedang dijalankan.

Contoh

```python
angka = int(input("Masukkan Angka : "))
```

Pengguna memasukkan

```
abc
```

Output

```
ValueError
```

Karena huruf tidak dapat diubah menjadi Integer.

---

Contoh lain

```python
print(10 / 0)
```

Output

```
ZeroDivisionError
```

Karena angka tidak dapat dibagi dengan nol.

---

# 3. Logical Error

Logical Error adalah Error yang paling sulit ditemukan.

Program tetap berjalan, tetapi hasilnya salah.

Contoh

```python
panjang = 10
lebar = 5

luas = panjang + lebar

print(luas)
```

Output

```
15
```

Padahal rumus luas persegi panjang seharusnya

```
panjang × lebar
```

Perbaikan

```python
luas = panjang * lebar
```

---

# Membaca Error Message

Ketika terjadi Error, Python akan menampilkan pesan.

Contoh

```
NameError:
name 'umur' is not defined
```

Artinya

Variable

```
umur
```

belum pernah dibuat.

---

Contoh

```python
print(nama)
```

Padahal

```python
nama
```

belum ada.

---

# Cara Melakukan Debugging

Langkah pertama.

Baca Error Message.

↓

Cari baris yang menyebabkan Error.

↓

Pahami penyebabnya.

↓

Perbaiki kode.

↓

Jalankan kembali program.

---

# Teknik Debugging Sederhana

Salah satu cara paling mudah adalah menggunakan

```python
print()
```

Contoh

```python
angka = 10

print(angka)

hasil = angka * 5

print(hasil)
```

Dengan begitu kita dapat melihat isi variable selama program berjalan.

---

# Contoh Program Salah

```python
umur = input("Umur : ")

print(umur + 5)
```

Output

```
TypeError
```

Karena

```
umur
```

bertipe String.

Perbaikan

```python
umur = int(input("Umur : "))

print(umur + 5)
```

---

# Contoh Program Benar

```python
angka1 = int(input("Angka Pertama : "))
angka2 = int(input("Angka Kedua : "))

hasil = angka1 + angka2

print("Hasil :", hasil)
```

---

# Diagram Debugging

```
Program Error

↓

Baca Error Message

↓

Cari Baris Error

↓

Perbaiki Kode

↓

Jalankan Lagi

↓

Program Berhasil
```

---

# Tips Debugging

✔ Baca pesan Error dengan teliti.

✔ Jangan langsung menghapus banyak kode.

✔ Periksa satu Error dalam satu waktu.

✔ Gunakan `print()` untuk melihat isi variable.

✔ Jalankan program kembali setelah diperbaiki.

---

# Project Hari Ini

## Guessing Number

Buat permainan sederhana.

Program menentukan angka rahasia.

Contoh

```
7
```

Kemudian pengguna diminta menebak angka tersebut.

Jika tebakan benar.

```
Selamat!

Jawaban Anda Benar!
```

Jika salah.

```
Jawaban Masih Salah

Silakan Coba Lagi
```

Gunakan:

- Variable
- While Loop
- IF
- Input

Contoh

```
=========================
GUESSING NUMBER
=========================

Tebak Angka (1-10)

> 4

Jawaban Salah

> 7

Selamat!

Jawaban Anda Benar!
```

---

# Challenge 1

Tambahkan petunjuk.

Jika angka terlalu kecil.

```
Terlalu Kecil
```

Jika angka terlalu besar.

```
Terlalu Besar
```

---

# Challenge 2

Hitung jumlah percobaan.

Contoh

```
Selamat!

Anda berhasil menebak dalam

5 percobaan.
```

---

# Challenge 3

Batasi jumlah percobaan sebanyak

```
5 kali
```

Jika gagal.

```
Game Over

Jawaban yang benar adalah 7
```

---

# Mini Challenge

Buat salah satu permainan berikut.

- Tebak Warna
- Tebak Huruf
- Tebak Hewan
- Tebak Buah
- Tebak Kota
- Tebak Nama Tokoh

Gunakan:

- While Loop
- IF
- Variable
- Counter

---

# Latihan Debugging

Perbaiki program berikut.

## Soal 1

```python
umur = input("Umur : ")

print(umur + 5)
```

Apa penyebab Error?

---

## Soal 2

```python
nilai = 80

if nilai >= 75
    print("Lulus")
```

Apa yang kurang?

---

## Soal 3

```python
def luas(panjang, lebar):

    return panjang + lebar
```

Mengapa hasilnya salah?

---

## Soal 4

```python
for i in range(5)

    print(i)
```

Apa yang menyebabkan Syntax Error?

---

# Kesalahan yang Sering Terjadi

❌ Tidak membaca Error Message.

Biasakan membaca Error dari atas hingga bawah sebelum memperbaiki kode.

---

❌ Langsung mengubah banyak bagian kode sekaligus.

Perbaiki satu Error terlebih dahulu, kemudian jalankan kembali program.

---

❌ Salah mengubah tipe data.

Contoh

```python
umur = input()
```

Padahal akan digunakan untuk perhitungan.

Gunakan

```python
umur = int(input())
```

---

❌ Menganggap semua Error berasal dari Python.

Sebagian besar Error justru berasal dari logika yang kita tulis.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Apa itu Bug

✅ Apa itu Debugging

✅ Syntax Error

✅ Runtime Error

✅ Logical Error

✅ Membaca Error Message

✅ Teknik Debugging menggunakan `print()`

✅ Cara memperbaiki program yang Error

✅ Membuat Guessing Number

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan mulai **Final Project**.

Kita akan belajar:

- Menentukan ide proyek.
- Membuat Flowchart.
- Merancang algoritma.
- Menggabungkan seluruh materi Python yang telah dipelajari.
- Memulai pembuatan Free Project.
