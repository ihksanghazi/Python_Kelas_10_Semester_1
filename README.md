# Pertemuan 15 — Final Project (Design & Development)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Free Project (Perancangan & Pengembangan)

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Menentukan ide proyek secara mandiri.
- Membuat Flowchart sederhana sebelum mulai coding.
- Menggabungkan seluruh materi Python yang telah dipelajari.
- Menyusun program secara terstruktur menggunakan Function.
- Melakukan debugging secara mandiri.
- Memulai pengembangan Final Project.

---

# Review Semester Ini

Selama satu semester kita telah mempelajari berbagai konsep dasar Python.

Materi yang telah dipelajari:

✅ Python Dasar

✅ Input & Output

✅ Variable

✅ Tipe Data

✅ String Formatting

✅ Library

✅ Operator

✅ Conditional

✅ Nested IF

✅ Looping

✅ Nested Loop

✅ Function

✅ Parameter & Return

✅ Debugging

Hari ini kita akan menggabungkan seluruh materi tersebut menjadi sebuah proyek.

---

# Apa itu Final Project?

Final Project adalah proyek yang dibuat untuk menunjukkan bahwa kita telah memahami seluruh materi selama satu semester.

Pada proyek ini siswa bebas memilih ide aplikasi yang ingin dibuat.

Yang terpenting adalah program dapat berjalan dengan baik.

---

# Tahapan Membuat Program

Seorang programmer biasanya mengikuti tahapan berikut.

```
Ide

↓

Flowchart

↓

Coding

↓

Testing

↓

Debugging

↓

Program Selesai
```

Jangan langsung menulis kode tanpa membuat rencana terlebih dahulu.

---

# Menentukan Ide

Pilih proyek yang sederhana tetapi menarik.

Contoh:

- Kasir Mini
- Login Sederhana
- Data Siswa
- Tebak Angka
- Kalkulator
- Jadwal Pelajaran
- Sistem Nilai
- Daftar Belanja
- Pendaftaran Lomba
- Menu Restoran

Pilih proyek yang sesuai dengan kemampuan.

---

# Mengenal Flowchart

Flowchart adalah diagram yang menggambarkan alur kerja program.

Flowchart membantu kita memahami urutan proses sebelum mulai menulis kode.

---

# Simbol Flowchart Dasar

## Start / End

```
(Oval)

Mulai

Selesai
```

---

## Process

```
[ Persegi Panjang ]

Menghitung Total

Menyimpan Data
```

---

## Input / Output

```
/ Jajar Genjang /

Masukkan Nama

Tampilkan Hasil
```

---

## Decision

```
< Belah Ketupat >

Apakah Nilai >= 75 ?

Ya / Tidak
```

---

# Contoh Flowchart

Program Kelulusan

```
Mulai

↓

Input Nama

↓

Input Nilai

↓

Nilai >= 75 ?

↓

Ya --------> Lulus

↓

Tidak -----> Tidak Lulus

↓

Selesai
```

---

# Membagi Program Menjadi Beberapa Bagian

Program yang baik terdiri dari beberapa bagian.

Misalnya

```
Menu

↓

Input

↓

Perhitungan

↓

Output

↓

Selesai
```

Jika memungkinkan gunakan Function agar program lebih rapi.

---

# Menggunakan Function

Contoh

```python
def menu():
    pass

def input_data():
    pass

def proses():
    pass

def output():
    pass
```

Program menjadi lebih mudah dibaca dibandingkan semua kode ditulis dalam satu tempat.

---

# Materi yang Sebaiknya Digunakan

Usahakan Final Project menggunakan beberapa konsep berikut.

- input()
- print()
- Variable
- Operator
- IF
- Loop
- Function

Semakin banyak konsep yang digunakan, semakin baik latihan yang diperoleh.

---

# Contoh Struktur Program

```python
def tampil_judul():
    print("======================")
    print("TOKO MINI")
    print("======================")

def hitung_total(harga, jumlah):
    return harga * jumlah

tampil_judul()

harga = int(input("Harga : "))
jumlah = int(input("Jumlah : "))

total = hitung_total(harga, jumlah)

print("Total :", total)
```

---

# Testing Program

Setelah selesai menulis kode, lakukan pengujian.

Coba berbagai kemungkinan.

Contoh

Input benar.

```
Harga : 10000

Jumlah : 2
```

Apakah hasilnya benar?

---

Coba juga input yang berbeda.

```
Harga : 0

Jumlah : 5
```

Apakah program masih berjalan?

---

# Debugging

Jika terjadi Error.

Lakukan langkah berikut.

1. Baca Error Message.
2. Cari baris yang bermasalah.
3. Perbaiki Error.
4. Jalankan kembali program.

Jangan langsung mengubah seluruh kode.

---

# Checklist Final Project

Sebelum proyek dianggap selesai, pastikan.

☐ Program dapat dijalankan.

☐ Tidak ada Syntax Error.

☐ Tidak ada Runtime Error.

☐ Output sesuai harapan.

☐ Nama variable mudah dipahami.

☐ Kode memiliki indentasi yang rapi.

☐ Menggunakan Function.

☐ Menggunakan minimal satu percabangan.

☐ Menggunakan minimal satu perulangan.

---

# Project Hari Ini

## Free Project (Tahap Perancangan & Pengembangan)

Siswa bebas memilih salah satu proyek berikut atau membuat ide sendiri.

### Pilihan 1

Kasir Sederhana

---

### Pilihan 2

Login Sederhana

---

### Pilihan 3

Sistem Penilaian Siswa

---

### Pilihan 4

Kalkulator

---

### Pilihan 5

Perpustakaan Mini

---

### Pilihan 6

Daftar Belanja

---

### Pilihan 7

Pendaftaran Lomba

---

### Pilihan 8

Quiz Sederhana

---

### Pilihan 9

Game Tebak Angka

---

### Pilihan 10

Ide Bebas

---

# Persyaratan Project

Project minimal harus menggunakan:

✅ Input

✅ Output

✅ Variable

✅ Operator

✅ IF

✅ Loop

✅ Function

Selain itu, siswa harus membuat **Flowchart sederhana** sebelum mulai menulis kode.

---

# Challenge 1

Tambahkan menu utama.

Contoh

```
=====================

MENU

1. Mulai

2. Bantuan

3. Keluar

=====================
```

---

# Challenge 2

Buat tampilan program lebih menarik menggunakan.

- Garis pembatas
- Judul
- f-string
- String Formatting

---

# Challenge 3

Tambahkan validasi input agar program tidak mudah mengalami Error.

Contoh

```
Input Tidak Valid
```

---

# Tips Mengerjakan Final Project

✔ Tentukan tujuan program terlebih dahulu.

✔ Buat Flowchart sebelum coding.

✔ Kerjakan sedikit demi sedikit.

✔ Uji program setiap selesai menambahkan fitur.

✔ Simpan file secara berkala.

✔ Jangan takut melakukan debugging.

---

# Rubrik Penilaian

| Aspek               | Penilaian  |
| ------------------- | ---------- |
| Program Berjalan    | ⭐⭐⭐⭐⭐ |
| Flowchart           | ⭐⭐⭐⭐⭐ |
| Penggunaan Function | ⭐⭐⭐⭐⭐ |
| Logika Program      | ⭐⭐⭐⭐⭐ |
| Tampilan Output     | ⭐⭐⭐⭐⭐ |
| Kerapihan Kode      | ⭐⭐⭐⭐⭐ |

---

# Ringkasan

Hari ini kita telah belajar:

✅ Menentukan ide proyek

✅ Membuat Flowchart

✅ Menyusun struktur program

✅ Menggabungkan seluruh materi Python

✅ Testing Program

✅ Debugging

✅ Memulai Final Project

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan:

- Menyelesaikan Final Project.
- Melakukan Code Review.
- Mempresentasikan hasil karya di depan kelas.
- Memberikan dan menerima umpan balik.
- Melakukan refleksi pembelajaran selama satu semester.
