# Pertemuan 7 — Conditional (IF, ELIF, ELSE)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Cek Kelulusan Siswa

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep pengambilan keputusan (Decision Making).
- Memahami fungsi `if`, `elif`, dan `else`.
- Memahami pentingnya indentasi pada Python.
- Menggunakan operator comparison dan logical pada percabangan.
- Membuat program sederhana yang dapat mengambil keputusan.
- Membuat aplikasi Cek Kelulusan Siswa.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Operator Aritmatika
- Operator Assignment
- Operator Comparison
- Operator Logical

Hari ini kita akan menggunakan semua operator tersebut untuk membuat komputer **mengambil keputusan**.

---

# Apa itu Conditional?

Conditional adalah proses pengambilan keputusan berdasarkan suatu kondisi.

Contoh dalam kehidupan sehari-hari:

```
Jika hujan
→ membawa payung

Jika tidak hujan
→ tidak membawa payung
```

Komputer juga bekerja dengan cara yang sama.

---

# Mengapa Conditional Dibutuhkan?

Banyak program menggunakan percabangan.

Contohnya:

- Login akun
- ATM
- Mesin kasir
- Game
- Sistem absensi
- Penilaian siswa

Semua program tersebut harus memilih tindakan berdasarkan kondisi tertentu.

---

# Struktur IF

Sintaks dasar

```python
if kondisi:
    perintah
```

Contoh

```python
umur = 18

if umur >= 17:
    print("Boleh Membuat SIM")
```

Output

```
Boleh Membuat SIM
```

---

# Bagaimana IF Bekerja?

Program membaca kondisi terlebih dahulu.

```
Apakah umur >= 17 ?

Ya
↓

Jalankan kode

Tidak
↓

Lewati kode
```

---

# Contoh Lain

```python
nilai = 90

if nilai >= 75:
    print("Lulus")
```

Output

```
Lulus
```

---

Jika nilainya

```python
nilai = 60
```

Maka tidak ada output karena kondisi bernilai **False**.

---

# Mengenal ELSE

`else` dijalankan ketika kondisi pada `if` bernilai **False**.

Contoh

```python
nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Output

```
Tidak Lulus
```

---

# Alur IF ELSE

```
        Kondisi

        True
          │
          ▼
     Jalankan IF

        False
          │
          ▼
    Jalankan ELSE
```

---

# Mengenal ELIF

Kadang kita memiliki lebih dari dua pilihan.

Gunakan

```python
elif
```

Contoh

```python
nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
else:
    print("Grade C")
```

Output

```
Grade B
```

---

# Urutan Pemeriksaan

Python membaca kondisi dari atas ke bawah.

Jika salah satu kondisi sudah benar, maka kondisi berikutnya tidak diperiksa lagi.

Contoh

```python
nilai = 95

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
else:
    print("C")
```

Output

```
A
```

---

# Pentingnya Indentasi

Python menggunakan indentasi untuk menentukan blok kode.

Contoh yang benar

```python
if nilai >= 75:
    print("Lulus")
```

---

Contoh yang salah

```python
if nilai >= 75:
print("Lulus")
```

Python akan menghasilkan error.

Gunakan **4 spasi** atau **1 tombol Tab** setelah tanda titik dua (`:`).

---

# Menggunakan Operator Comparison

```python
umur = 20

if umur >= 17:
    print("Dewasa")
```

Operator yang sering digunakan:

- >
- <
- > =
- <=
- ==
- !=

---

# Menggunakan Operator Logical

Contoh

```python
umur = 20

if umur >= 17 and umur <= 25:
    print("Remaja Akhir")
```

Kedua kondisi harus bernilai True.

---

Contoh menggunakan OR

```python
hari = "Sabtu"

if hari == "Sabtu" or hari == "Minggu":
    print("Libur")
```

Output

```
Libur
```

---

# Contoh Program

```python
nilai = int(input("Masukkan Nilai : "))

if nilai >= 75:
    print("Selamat, Anda Lulus!")
else:
    print("Maaf, Anda Belum Lulus.")
```

Output

```
Masukkan Nilai : 85

Selamat, Anda Lulus!
```

---

# Menentukan Grade

```python
nilai = int(input("Nilai : "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")
```

---

# Diagram Percabangan

```
          Nilai

            │
            ▼

      Nilai >= 75 ?

       ┌──────────┐
     Ya│          │Tidak
       ▼          ▼

    LULUS     TIDAK LULUS
```

---

# Project Hari Ini

## Cek Kelulusan Siswa

Buat program yang meminta pengguna memasukkan:

- Nama Siswa
- Nilai

Kemudian tampilkan hasilnya.

Aturan:

```
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Contoh

```
==========================
CEK KELULUSAN SISWA
==========================

Nama  : Andi
Nilai : 88

Status : LULUS

==========================
```

---

# Challenge 1

Tambahkan penilaian Grade.

Aturan

```
90 - 100 → A

80 - 89 → B

70 - 79 → C

< 70 → D
```

Contoh

```
Nama : Sandy

Nilai : 95

Grade : A
```

---

# Challenge 2

Tambahkan kategori.

```
A → Sangat Baik

B → Baik

C → Cukup

D → Perlu Belajar Lagi
```

---

# Challenge 3

Tambahkan validasi nilai.

Jika nilai

```
< 0
```

atau

```
> 100
```

Program menampilkan

```
Input Tidak Valid
```

---

# Mini Challenge

Buat salah satu program berikut.

- Penentu Diskon Belanja
- Penentu Umur (Anak, Remaja, Dewasa)
- Login Sederhana
- Penentu Cuaca
- Penilaian Film
- Penentu Kelulusan Ujian SIM

Gunakan minimal:

- 1 IF
- 2 ELIF
- 1 ELSE

---

# Kesalahan yang Sering Terjadi

❌ Menggunakan `=` pada kondisi.

Salah

```python
if nilai = 75:
```

Benar

```python
if nilai == 75:
```

---

❌ Lupa tanda titik dua (`:`)

Salah

```python
if nilai >= 75
```

Benar

```python
if nilai >= 75:
```

---

❌ Indentasi salah

Salah

```python
if nilai >= 75:
print("Lulus")
```

Benar

```python
if nilai >= 75:
    print("Lulus")
```

---

❌ Urutan kondisi salah

Salah

```python
if nilai >= 70:
    print("C")
elif nilai >= 90:
    print("A")
```

Karena nilai 95 akan langsung masuk ke kondisi pertama.

Urutan yang benar dimulai dari nilai tertinggi.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Konsep Conditional

✅ IF

✅ ELSE

✅ ELIF

✅ Indentasi Python

✅ Operator Comparison

✅ Operator Logical

✅ Membuat keputusan pada program

✅ Membuat aplikasi Cek Kelulusan Siswa

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Nested IF (IF di dalam IF)
- Percabangan bertingkat
- Menggabungkan banyak kondisi
- Studi kasus logika kompleks
- Project: Aplikasi Pembuatan SIM
