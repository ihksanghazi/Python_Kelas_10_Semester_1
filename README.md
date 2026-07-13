# Pertemuan 8 — Nested Conditional (Nested IF)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Aplikasi Pembuatan SIM

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep Nested IF.
- Mengetahui perbedaan IF biasa dan Nested IF.
- Membuat percabangan bertingkat.
- Menggabungkan beberapa kondisi dalam satu program.
- Menganalisis alur logika yang kompleks.
- Membuat simulasi Aplikasi Pembuatan SIM.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- IF
- ELIF
- ELSE
- Operator Comparison
- Operator Logical
- Pengambilan Keputusan

Hari ini kita akan membuat keputusan yang lebih kompleks menggunakan **Nested IF**.

---

# Apa itu Nested IF?

Nested IF adalah **IF di dalam IF**.

Artinya, setelah suatu kondisi terpenuhi, program akan memeriksa kondisi berikutnya.

Contoh kehidupan sehari-hari.

```
Apakah umur sudah 17 tahun?

↓

Ya

↓

Apakah sudah lulus tes kesehatan?

↓

Ya

↓

Apakah lulus ujian praktik?

↓

Ya

↓

SIM dapat dibuat.
```

Karena terdapat beberapa tahapan pemeriksaan, kita membutuhkan Nested IF.

---

# Perbedaan IF Biasa dan Nested IF

## IF Biasa

Hanya memeriksa satu kondisi.

```python
umur = 18

if umur >= 17:
    print("Boleh Membuat SIM")
```

---

## Nested IF

Memeriksa beberapa kondisi secara bertahap.

```python
umur = 18
sehat = True

if umur >= 17:
    if sehat:
        print("Boleh Mengikuti Tes SIM")
```

Program hanya masuk ke IF kedua jika IF pertama bernilai **True**.

---

# Struktur Nested IF

```python
if kondisi_1:
    if kondisi_2:
        print("Aksi")
```

Urutan pemeriksaan:

```
Kondisi 1

↓

Jika True

↓

Kondisi 2

↓

Jika True

↓

Program dijalankan
```

---

# Contoh Sederhana

```python
umur = 20
punya_ktp = True

if umur >= 17:
    if punya_ktp:
        print("Silakan Daftar")
```

Output

```
Silakan Daftar
```

---

# Contoh Dengan ELSE

```python
umur = 16

if umur >= 17:
    print("Cukup Umur")
else:
    print("Belum Cukup Umur")
```

Output

```
Belum Cukup Umur
```

---

# Nested IF dengan ELSE

```python
umur = 20
punya_ktp = False

if umur >= 17:
    if punya_ktp:
        print("Pendaftaran Berhasil")
    else:
        print("Harus Memiliki KTP")
else:
    print("Belum Cukup Umur")
```

Output

```
Harus Memiliki KTP
```

---

# Menggunakan Input

Nested IF dapat digabungkan dengan input.

```python
umur = int(input("Masukkan Umur : "))
```

Kemudian

```python
if umur >= 17:
    print("Boleh Daftar")
else:
    print("Belum Boleh")
```

---

# Menggunakan Operator Logical

Contoh

```python
umur = 20
sehat = True

if umur >= 17:
    if sehat == True:
        print("Lolos Tahap Awal")
```

Atau lebih sederhana.

```python
if umur >= 17:
    if sehat:
        print("Lolos Tahap Awal")
```

---

# Diagram Nested IF

```
              Umur >= 17 ?

              Ya
              │
              ▼

        Punya KTP ?

          Ya
          │
          ▼

      Lulus Tes Kesehatan ?

          Ya
          │
          ▼

     BOLEH MEMBUAT SIM
```

---

# Contoh Program

```python
umur = int(input("Masukkan Umur : "))
ktp = input("Punya KTP? (ya/tidak) : ")

if umur >= 17:
    if ktp == "ya":
        print("Silakan Mengikuti Tes SIM")
    else:
        print("Harus Memiliki KTP")
else:
    print("Belum Cukup Umur")
```

---

# Studi Kasus

Syarat membuat SIM:

- Umur minimal 17 tahun.
- Memiliki KTP.
- Lulus Tes Kesehatan.

Jika salah satu syarat tidak terpenuhi, program harus memberikan alasan mengapa pendaftaran ditolak.

---

# Alur Program

```
Mulai

↓

Input Umur

↓

Apakah umur >= 17?

↓

Tidak
↓

Gagal

↓

Ya

↓

Punya KTP?

↓

Tidak
↓

Gagal

↓

Ya

↓

Lulus Tes Kesehatan?

↓

Tidak
↓

Gagal

↓

Ya

↓

Pendaftaran Berhasil
```

---

# Project Hari Ini

## Aplikasi Pembuatan SIM

Buat program yang meminta pengguna memasukkan:

- Nama
- Umur
- Memiliki KTP? (ya/tidak)
- Lulus Tes Kesehatan? (ya/tidak)

Kemudian tampilkan hasilnya.

Contoh

```
==========================
PENDAFTARAN SIM
==========================

Nama : Andi

Status :

Pendaftaran Berhasil

==========================
```

Jika gagal.

Contoh

```
==========================

Nama : Andi

Status :

Belum Cukup Umur

==========================
```

Atau

```
Harus Memiliki KTP
```

Atau

```
Tidak Lulus Tes Kesehatan
```

---

# Challenge 1

Tambahkan satu syarat lagi.

```
Lulus Tes Teori
```

Program hanya menerima peserta jika semua syarat terpenuhi.

---

# Challenge 2

Tambahkan kategori SIM.

```
SIM A

SIM C
```

Jika memilih selain dua pilihan tersebut.

Tampilkan

```
Jenis SIM Tidak Tersedia
```

---

# Challenge 3

Tambahkan hasil akhir.

Jika seluruh syarat terpenuhi.

```
========================

Selamat!

Anda Berhasil Mendaftar SIM

Silakan Menunggu Jadwal Ujian

========================
```

Jika gagal.

```
Mohon Lengkapi Persyaratan Terlebih Dahulu
```

---

# Mini Challenge

Buat salah satu simulasi berikut menggunakan Nested IF.

- Login ATM
- Registrasi Sekolah
- Booking Hotel
- Pendaftaran Turnamen Game
- Seleksi Organisasi
- Registrasi Event

Gunakan minimal **3 syarat** sebelum program menyatakan berhasil.

---

# Tips Membuat Nested IF

✔ Gunakan Nested IF jika proses pemeriksaan dilakukan **bertahap**.

✔ Gunakan nama variable yang jelas.

✔ Pastikan indentasi rapi agar program mudah dibaca.

✔ Berikan pesan yang berbeda untuk setiap kondisi gagal agar pengguna mengetahui penyebabnya.

---

# Kesalahan yang Sering Terjadi

❌ Lupa indentasi.

Salah

```python
if umur >= 17:
if ktp == "ya":
    print("Lolos")
```

Benar

```python
if umur >= 17:
    if ktp == "ya":
        print("Lolos")
```

---

❌ Menggunakan `=` pada kondisi.

Salah

```python
if ktp = "ya":
```

Benar

```python
if ktp == "ya":
```

---

❌ Salah menempatkan `else`.

Salah

```python
if umur >= 17:
    if ktp == "ya":
        print("Lolos")
else:
    print("Gagal")
```

Pastikan `else` memiliki pasangan `if` yang sesuai.

---

❌ Terlalu banyak Nested IF.

Jika percabangan mulai terlalu dalam (lebih dari 3–4 tingkat), pertimbangkan menggunakan `elif` atau menggabungkan kondisi dengan operator logical agar kode lebih mudah dibaca.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Konsep Nested IF

✅ Perbedaan IF dan Nested IF

✅ Percabangan Bertingkat

✅ Nested IF dengan ELSE

✅ Menggabungkan Input dan Nested IF

✅ Menggunakan Operator Logical

✅ Membuat Simulasi Pendaftaran SIM

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Perulangan (Looping)
- While Loop
- For Loop
- Fungsi `range()`
- Menghindari Infinite Loop
- Project: Password Checker & Tabel Perkalian
