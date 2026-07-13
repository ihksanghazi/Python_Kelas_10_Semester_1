# Pertemuan 6 — Basic Operations (Operator pada Python)

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Kasir Sederhana

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami fungsi operator dalam Python.
- Menggunakan Operator Aritmatika.
- Menggunakan Operator Assignment.
- Menggunakan Operator Comparison.
- Menggunakan Operator Logical.
- Menggabungkan operator dalam sebuah program.
- Membuat program Kasir Sederhana.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Library Python
- import
- random
- time
- os

Hari ini kita akan belajar bagaimana komputer **menghitung**, **membandingkan**, dan **mengambil keputusan** menggunakan operator.

---

# Apa itu Operator?

Operator adalah simbol yang digunakan untuk melakukan suatu operasi pada data.

Contohnya:

```
+
-
*
/
==
>
<
```

Operator membantu komputer melakukan berbagai perhitungan dan logika.

---

# Jenis Operator

Hari ini kita akan mempelajari empat jenis operator.

- Operator Aritmatika
- Operator Assignment
- Operator Comparison
- Operator Logical

---

# Operator Aritmatika

Operator aritmatika digunakan untuk melakukan perhitungan matematika.

| Operator | Fungsi             |
| -------- | ------------------ |
| +        | Penjumlahan        |
| -        | Pengurangan        |
| \*       | Perkalian          |
| /        | Pembagian          |
| //       | Pembagian Bulat    |
| %        | Sisa Bagi (Modulo) |
| \*\*     | Pangkat            |

---

# Penjumlahan

```python
a = 10
b = 5

print(a + b)
```

Output

```
15
```

---

# Pengurangan

```python
print(10 - 4)
```

Output

```
6
```

---

# Perkalian

```python
print(8 * 3)
```

Output

```
24
```

---

# Pembagian

```python
print(10 / 2)
```

Output

```
5.0
```

Perhatikan bahwa hasil pembagian selalu bertipe **float**.

---

# Pembagian Bulat

```python
print(10 // 3)
```

Output

```
3
```

Bagian desimal akan dibuang.

---

# Modulo (%)

Modulo digunakan untuk mencari sisa hasil pembagian.

```python
print(10 % 3)
```

Output

```
1
```

Contoh lain

```
8 % 2 = 0
```

Artinya 8 habis dibagi 2.

Modulo sering digunakan untuk mengecek bilangan genap dan ganjil.

---

# Pangkat

```python
print(2 ** 3)
```

Output

```
8
```

Karena

```
2 × 2 × 2 = 8
```

---

# Operator Assignment

Operator Assignment digunakan untuk memberikan atau memperbarui nilai suatu variable.

Operator yang sering digunakan:

| Operator | Contoh  |
| -------- | ------- |
| =        | x = 5   |
| +=       | x += 2  |
| -=       | x -= 2  |
| \*=      | x \*= 2 |
| /=       | x /= 2  |

---

# Assignment Dasar

```python
score = 100
```

Artinya

```
Masukkan nilai 100 ke dalam variable score.
```

---

# Operator +=

```python
score = 100

score += 20

print(score)
```

Output

```
120
```

Sama dengan

```python
score = score + 20
```

---

# Operator -=

```python
uang = 50000

uang -= 10000

print(uang)
```

Output

```
40000
```

---

# Operator \*=

```python
jumlah = 5

jumlah *= 3

print(jumlah)
```

Output

```
15
```

---

# Operator Comparison

Operator Comparison digunakan untuk membandingkan dua nilai.

Hasilnya selalu:

```
True
```

atau

```
False
```

---

| Operator | Arti                  |
| -------- | --------------------- |
| ==       | Sama dengan           |
| !=       | Tidak sama dengan     |
| >        | Lebih besar           |
| <        | Lebih kecil           |
| >=       | Lebih besar atau sama |
| <=       | Lebih kecil atau sama |

---

# Contoh Comparison

```python
print(10 > 5)
```

Output

```
True
```

---

```python
print(3 > 7)
```

Output

```
False
```

---

```python
print(10 == 10)
```

Output

```
True
```

---

```python
print(10 != 5)
```

Output

```
True
```

---

# Operator Logical

Operator Logical digunakan untuk menggabungkan beberapa kondisi.

Operator yang digunakan:

| Operator | Fungsi                   |
| -------- | ------------------------ |
| and      | Semua kondisi harus True |
| or       | Salah satu kondisi True  |
| not      | Membalik hasil           |

---

# Operator AND

```python
umur = 18

print(umur >= 17 and umur <= 25)
```

Output

```
True
```

Karena kedua kondisi benar.

---

# Operator OR

```python
print(10 > 20 or 10 < 20)
```

Output

```
True
```

Karena salah satu kondisi benar.

---

# Operator NOT

```python
print(not True)
```

Output

```
False
```

---

```python
print(not False)
```

Output

```
True
```

---

# Menggabungkan Operator

Contoh

```python
harga = 5000
jumlah = 3

total = harga * jumlah

print(total)
```

Output

```
15000
```

---

# Contoh Program

```python
harga = int(input("Harga Barang : "))
jumlah = int(input("Jumlah Barang : "))

total = harga * jumlah

print()
print("===== STRUK PEMBELIAN =====")
print(f"Harga Barang : Rp {harga}")
print(f"Jumlah Barang : {jumlah}")
print(f"Total Bayar : Rp {total}")
```

Output

```
Harga Barang : 5000
Jumlah Barang : 4

===== STRUK PEMBELIAN =====
Harga Barang : Rp 5000
Jumlah Barang : 4
Total Bayar : Rp 20000
```

---

# Project Hari Ini

## Kasir Sederhana

Buat program yang meminta pengguna memasukkan:

- Nama Barang
- Harga Barang
- Jumlah Barang

Program kemudian menghitung:

```
Total = Harga × Jumlah
```

Lalu tampilkan hasilnya dalam bentuk struk.

Contoh

```
===========================
      MINI CASHIER
===========================

Nama Barang  : Pensil
Harga        : Rp 5.000
Jumlah       : 4

---------------------------
Total Bayar  : Rp 20.000
===========================
```

---

# Challenge 1

Tambahkan fitur:

- Diskon 10%
- Hitung Total Setelah Diskon

Contoh

```
Subtotal : Rp 100000
Diskon   : Rp 10000

Total    : Rp 90000
```

---

# Challenge 2

Tambahkan input:

- Uang Pembeli

Kemudian hitung

```
Kembalian
```

Contoh

```
Total Bayar : Rp 45000

Uang Pembeli : Rp 50000

Kembalian : Rp 5000
```

---

# Challenge 3

Gunakan Operator Comparison.

Jika uang pembeli kurang.

Tampilkan

```
Uang Tidak Cukup
```

Jika cukup.

Tampilkan

```
Terima Kasih Sudah Berbelanja
```

---

# Mini Challenge

Buat program kasir untuk salah satu tempat berikut.

- Toko Buku
- Minimarket
- Toko Game
- Toko Komputer
- Kafetaria Sekolah
- Bioskop

Tambahkan minimal **5 barang** beserta harga masing-masing.

---

# Kesalahan yang Sering Terjadi

❌ Menggunakan `=` untuk membandingkan nilai.

Salah

```python
print(10 = 10)
```

Benar

```python
print(10 == 10)
```

---

❌ Lupa mengubah input menjadi Integer.

Salah

```python
harga = input("Harga : ")
jumlah = input("Jumlah : ")

print(harga * jumlah)
```

Karena `input()` menghasilkan String.

Benar

```python
harga = int(input("Harga : "))
jumlah = int(input("Jumlah : "))
```

---

❌ Salah menggunakan operator logika.

Contoh

```python
umur >= 17 or umur <= 25
```

Hampir selalu bernilai True.

Yang benar

```python
umur >= 17 and umur <= 25
```

---

# Ringkasan

Hari ini kita telah belajar:

✅ Operator Aritmatika

✅ Operator Assignment

✅ Operator Comparison

✅ Operator Logical

✅ Menggabungkan beberapa operator

✅ Menghitung menggunakan operator

✅ Membuat Program Kasir Sederhana

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Conditional (IF)
- IF, ELIF, ELSE
- Indentasi pada Python
- Pengambilan Keputusan
- Project: Cek Kelulusan Siswa
