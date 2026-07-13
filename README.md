# Pertemuan 2 — Variable & Tipe Data Dasar Python

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Story Generator

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami apa itu variable.
- Memahami fungsi variable dalam pemrograman.
- Mengetahui aturan penamaan variable.
- Mengenal tipe data dasar Python.
- Menggunakan variable untuk menyimpan data.
- Membuat program Story Generator sederhana menggunakan variable.

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- Apa itu Python
- Fungsi `print()`
- Fungsi `input()`
- Konsep IPO (Input → Process → Output)

Hari ini kita akan belajar bagaimana komputer **menyimpan data**.

---

# Apa itu Variable?

Variable adalah tempat untuk menyimpan data di dalam program.

Bayangkan variable seperti sebuah kotak.

Di dalam kotak tersebut kita bisa menyimpan:

- Nama
- Umur
- Nilai
- Alamat
- Angka
- Tulisan

Contoh:

```
Kotak Nama
──────────────
Sandy
```

Di Python kita menulisnya seperti ini

```python
nama = "Sandy"
```

Artinya

```
Simpan tulisan "Sandy"
ke dalam variable bernama nama
```

---

# Kenapa Harus Menggunakan Variable?

Tanpa variable kita harus menulis data berulang kali.

Contoh

```python
print("Sandy")
print("Sandy")
print("Sandy")
```

Lebih baik

```python
nama = "Sandy"

print(nama)
print(nama)
print(nama)
```

Jika nama berubah, kita cukup mengubah satu baris saja.

---

# Cara Membuat Variable

Bentuk umum

```python
nama_variable = nilai
```

Contoh

```python
nama = "Andi"
umur = 16
tinggi = 170
```

---

# Menampilkan Isi Variable

Variable dapat ditampilkan menggunakan `print()`.

```python
nama = "Sandy"

print(nama)
```

Output

```
Sandy
```

---

# Mengubah Isi Variable

Isi variable bisa berubah.

```python
score = 50

print(score)

score = 100

print(score)
```

Output

```
50
100
```

Program akan menggunakan nilai terbaru.

---

# Aturan Penamaan Variable

Variable boleh menggunakan:

- Huruf
- Angka
- Underscore (\_)

Contoh

```python
nama
umur
student_name
nilai1
```

---

# Yang Tidak Boleh

Variable tidak boleh diawali angka.

❌ Salah

```python
1nama = "Andi"
```

✅ Benar

```python
nama1 = "Andi"
```

---

Tidak boleh memakai spasi.

❌ Salah

```python
full name = "Andi"
```

✅ Benar

```python
full_name = "Andi"
```

---

Tidak boleh memakai simbol.

❌ Salah

```python
nama!
nama@
nama#
```

---

Gunakan nama yang mudah dipahami.

❌ Kurang baik

```python
a = "Andi"
b = 16
```

✅ Lebih baik

```python
nama = "Andi"
umur = 16
```

---

# Mengenal Tipe Data

Data memiliki jenis yang berbeda.

Contoh

```
Nama
Umur
Tinggi
Sudah Lulus
```

Semuanya tidak memiliki jenis data yang sama.

---

# String (str)

String adalah data berupa teks.

Contoh

```python
nama = "Sandy"
kota = "Jakarta"
```

Output

```
Sandy
Jakarta
```

String selalu menggunakan:

```
" "
```

atau

```
' '
```

---

# Integer (int)

Integer adalah bilangan bulat.

Contoh

```python
umur = 16
nilai = 100
```

Output

```
16
100
```

Tidak memakai tanda kutip.

---

# Float (float)

Float adalah bilangan desimal.

Contoh

```python
tinggi = 170.5
berat = 55.8
```

Output

```
170.5
55.8
```

---

# Boolean (bool)

Boolean hanya memiliki dua nilai.

```
True
False
```

Contoh

```python
is_student = True
```

atau

```python
lampu_menyala = False
```

Boolean sering digunakan saat membuat logika program.

---

# Melihat Tipe Data

Python memiliki fungsi

```python
type()
```

Contoh

```python
nama = "Sandy"
umur = 16

print(type(nama))
print(type(umur))
```

Output

```
<class 'str'>
<class 'int'>
```

---

# Menggabungkan Variable

Kita bisa menampilkan beberapa variable sekaligus.

```python
nama = "Sandy"
umur = 16

print(nama, umur)
```

Output

```
Sandy 16
```

---

# Contoh Program

```python
nama = "Andi"
umur = 16
tinggi = 170.5

print(nama)
print(umur)
print(tinggi)
```

Output

```
Andi
16
170.5
```

---

# Project Hari Ini

## Story Generator

Siswa membuat cerita sederhana menggunakan beberapa variable.

Contoh

```python
nama = "Budi"
hewan = "Kucing"
tempat = "Pantai"

print(nama, "bermain bersama", hewan, "di", tempat)
```

Output

```
Budi bermain bersama Kucing di Pantai
```

---

# Challenge

Tambahkan variable berikut:

- makanan_favorit
- warna_favorit
- cita_cita
- sekolah
- hobi

Lalu buat cerita yang lebih panjang.

Contoh

```
Halo, nama saya Sandy.

Saya suka makan Bakso.

Hobi saya bermain basket.

Suatu hari saya pergi ke pantai bersama seekor kucing.

Cita-cita saya adalah menjadi Software Engineer.
```

Gunakan minimal **8 variable** dalam cerita.

---

# Ringkasan

Hari ini kita telah belajar:

✅ Apa itu Variable

✅ Cara membuat Variable

✅ Aturan penamaan Variable

✅ String (str)

✅ Integer (int)

✅ Float (float)

✅ Boolean (bool)

✅ Fungsi `type()`

✅ Membuat Story Generator menggunakan Variable

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Menggunakan `input()`
- Menggabungkan Input dan Variable
- Membuat program interaktif
- Konsep IPO dalam program nyata
- Project: Game Profile
