# Pertemuan 13 — Function dengan Parameter, Argument, dan Return Value

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Menghitung Luas Persegi Panjang

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami konsep Parameter dan Argument.
- Memahami perbedaan Parameter dan Argument.
- Menggunakan Function yang menerima data.
- Memahami fungsi `return`.
- Membuat Function yang mengembalikan hasil perhitungan.
- Membuat program menghitung luas persegi panjang menggunakan Function.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Function
- Keyword `def`
- Memanggil Function
- Manfaat Function

Hari ini kita akan membuat Function yang lebih pintar, yaitu Function yang bisa menerima data dan menghasilkan nilai.

---

# Apa itu Parameter?

Parameter adalah **variable** yang ditulis pada saat membuat Function.

Contoh

```python
def sapa(nama):

    print("Halo", nama)
```

Pada contoh di atas

```python
nama
```

adalah **Parameter**.

Parameter berfungsi sebagai tempat untuk menerima data.

---

# Apa itu Argument?

Argument adalah **nilai** yang dikirim ketika Function dipanggil.

Contoh

```python
sapa("Sandy")
```

Pada contoh di atas

```python
"Sandy"
```

adalah **Argument**.

Argument akan dikirim ke Parameter.

---

# Ilustrasi Parameter dan Argument

```
Function

↓

Parameter

↓

nama

↓

Argument

↓

"Sandy"

↓

Output

Halo Sandy
```

---

# Contoh Sederhana

```python
def sapa(nama):

    print("Halo", nama)

sapa("Andi")
```

Output

```
Halo Andi
```

---

# Mengirim Banyak Argument

Function dapat menerima lebih dari satu Parameter.

```python
def perkenalan(nama, umur):

    print("Nama :", nama)
    print("Umur :", umur)
```

Memanggil Function

```python
perkenalan("Sandy", 23)
```

Output

```
Nama : Sandy
Umur : 23
```

---

# Jumlah Parameter dan Argument

Jumlah Argument harus sama dengan jumlah Parameter.

Contoh yang benar

```python
def data(nama, umur):

    print(nama)
    print(umur)

data("Andi", 16)
```

---

Contoh yang salah

```python
data("Andi")
```

Python akan menghasilkan error karena jumlah datanya tidak sesuai.

---

# Apa itu Return Value?

Selama ini Function hanya menampilkan hasil menggunakan

```python
print()
```

Tetapi Function juga bisa **mengembalikan nilai**.

Caranya menggunakan

```python
return
```

---

# Function dengan Return

```python
def tambah(a, b):

    return a + b
```

Memanggil Function

```python
hasil = tambah(10, 5)

print(hasil)
```

Output

```
15
```

---

# Perbedaan print() dan return

## print()

Menampilkan hasil ke layar.

```python
def halo():

    print("Halo")
```

---

## return

Mengirim hasil kembali ke program.

```python
def tambah(a, b):

    return a + b
```

Nilai yang dikembalikan masih bisa disimpan ke dalam variable.

---

# Contoh Return

```python
def luas(panjang, lebar):

    return panjang * lebar

hasil = luas(10,5)

print(hasil)
```

Output

```
50
```

---

# Menyimpan Hasil Return

Karena menggunakan

```python
return
```

hasilnya dapat digunakan kembali.

```python
luas_kamar = luas(8,4)

print(luas_kamar)
```

---

# Diagram Function

```
Program

↓

Mengirim Argument

↓

Function

↓

Parameter

↓

Perhitungan

↓

Return

↓

Program Menerima Hasil
```

---

# Contoh Program

```python
def luas_persegi_panjang(panjang, lebar):

    return panjang * lebar

panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))

hasil = luas_persegi_panjang(panjang, lebar)

print("Luas =", hasil)
```

Output

```
Panjang : 10
Lebar : 6

Luas = 60
```

---

# Project Hari Ini

## Menghitung Luas Persegi Panjang

Buat sebuah Function.

```python
def hitung_luas(panjang, lebar):
```

Gunakan

```python
return
```

untuk mengembalikan hasil.

Program meminta pengguna memasukkan:

- Panjang
- Lebar

Kemudian tampilkan hasilnya.

Contoh

```
========================

LUAS PERSEGI PANJANG

========================

Panjang : 15

Lebar : 8

Luas : 120

========================
```

---

# Challenge 1

Tambahkan Function baru.

```python
def hitung_keliling(panjang, lebar):
```

Rumus

```
2 × (panjang + lebar)
```

Tampilkan hasilnya bersama luas.

---

# Challenge 2

Buat Function

```python
def salam(nama):
```

Output

```
Halo Sandy

Selamat Belajar Python!
```

Gunakan nama dari input pengguna.

---

# Challenge 3

Buat Function

```python
def hitung_diskon(harga):
```

Aturan

```
Diskon = 10%
```

Gunakan

```python
return
```

untuk mengembalikan harga setelah diskon.

---

# Mini Challenge

Buat salah satu program berikut menggunakan Function.

- Menghitung Luas Lingkaran
- Menghitung Luas Segitiga
- Menghitung Volume Kubus
- Konversi Suhu
- Menghitung Nilai Rata-rata
- Kalkulator Sederhana

Gunakan minimal:

- 2 Parameter
- 1 Return Value

---

# Tips

✔ Gunakan **Parameter** untuk menerima data.

✔ Gunakan **Argument** saat memanggil Function.

✔ Gunakan **return** jika hasil masih akan digunakan.

✔ Gunakan **print()** hanya untuk menampilkan hasil kepada pengguna.

✔ Berikan nama Function yang sesuai dengan tugasnya.

---

# Kesalahan yang Sering Terjadi

❌ Jumlah Parameter dan Argument tidak sama.

Salah

```python
def tambah(a, b):

    return a + b

tambah(10)
```

Benar

```python
tambah(10,5)
```

---

❌ Mengira `print()` sama dengan `return`.

Salah

```python
def tambah(a,b):

    print(a+b)

hasil = tambah(5,5)

print(hasil)
```

Output

```
10
None
```

Karena `print()` tidak mengembalikan nilai.

Gunakan

```python
return a+b
```

---

❌ Lupa menyimpan hasil Return.

Salah

```python
luas(5,10)
```

Benar

```python
hasil = luas(5,10)

print(hasil)
```

---

❌ Salah urutan Argument.

```python
luas(lebar, panjang)
```

Pastikan urutan Argument sesuai dengan Parameter yang dibuat.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Parameter

✅ Argument

✅ Perbedaan Parameter dan Argument

✅ Return Value

✅ Perbedaan `print()` dan `return`

✅ Function yang menerima data

✅ Function yang mengembalikan hasil

✅ Membuat Program Menghitung Luas Persegi Panjang

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Debugging
- Jenis-jenis Error
- Cara membaca Error Message
- Mencari dan memperbaiki Bug
- Project: Guessing Number (Aplikasi Kuis Interaktif)
