# Pertemuan 5 — Basic Python Library

> **Grade:** 10 SMA
> **Durasi:** 70 Menit
> **Platform:** Python
> **Project:** Dice Simulator

---

# Tujuan Pembelajaran

Pada akhir pembelajaran, siswa mampu:

- Memahami apa itu library pada Python.
- Menggunakan perintah `import`.
- Memahami fungsi library bawaan Python.
- Menggunakan library `random`, `time`, dan `os`.
- Membuat program simulasi lempar dadu (Dice Simulator).

---

# Review Pertemuan Sebelumnya

Pada pertemuan sebelumnya kita telah belajar:

- String Formatting
- f-string
- format()
- Escape Character
- Membuat tampilan output lebih rapi

Hari ini kita akan belajar menggunakan **library**, yaitu kumpulan kode yang sudah dibuat sehingga kita tidak perlu membuat semuanya dari awal.

---

# Apa itu Library?

Library adalah kumpulan fungsi yang telah dibuat oleh programmer lain sehingga bisa kita gunakan kembali.

Bayangkan seperti sebuah **kotak peralatan**.

Daripada membuat obeng sendiri, kita tinggal mengambil obeng dari kotak.

Begitu juga di Python.

Daripada membuat semuanya sendiri, kita cukup menggunakan library yang sudah tersedia.

---

# Kenapa Menggunakan Library?

Tanpa library kita harus membuat banyak kode sendiri.

Dengan library kita bisa:

- Menghemat waktu
- Membuat program lebih cepat
- Mengurangi jumlah kode
- Menggunakan fitur yang sudah terpercaya

---

# Mengenal import

Sebelum menggunakan library kita harus mengimpornya.

Contoh

```python
import random
```

Artinya

```
Gunakan library random.
```

---

# Library Bawaan Python

Python memiliki banyak library bawaan, contohnya:

- random
- math
- os
- time
- datetime

Hari ini kita akan mempelajari tiga library.

- random
- time
- os

---

# Library random

Library `random` digunakan untuk menghasilkan angka secara acak.

Import terlebih dahulu.

```python
import random
```

---

# random.randint()

Digunakan untuk menghasilkan angka acak dalam rentang tertentu.

Contoh

```python
import random

angka = random.randint(1, 6)

print(angka)
```

Output

```
4
```

Setiap program dijalankan, hasilnya bisa berbeda.

---

# Contoh Penggunaan

```python
import random

print(random.randint(1, 10))
```

Output bisa menjadi

```
2
```

atau

```
9
```

atau angka lain antara 1 sampai 10.

---

# Library time

Library `time` digunakan untuk mengatur waktu.

Import

```python
import time
```

---

# time.sleep()

Digunakan untuk memberi jeda.

Contoh

```python
import time

print("Loading...")

time.sleep(3)

print("Selesai")
```

Output

```
Loading...

(tunggu 3 detik)

Selesai
```

---

# Kenapa Menggunakan sleep()?

Agar program terasa lebih realistis.

Contohnya

- Loading game
- Mengunduh file
- Menghitung skor
- Melempar dadu

---

# Library os

Library `os` digunakan untuk berinteraksi dengan sistem operasi.

Import

```python
import os
```

---

# Membersihkan Layar

Pada Windows

```python
os.system("cls")
```

Pada Linux atau Mac

```python
os.system("clear")
```

Program akan membersihkan tampilan terminal.

---

# Menggabungkan Library

Kita dapat menggunakan lebih dari satu library.

```python
import random
import time
import os
```

Semuanya dapat digunakan dalam satu program.

---

# Contoh Program

```python
import random
import time

print("Rolling Dice...")

time.sleep(2)

print(random.randint(1,6))
```

Output

```
Rolling Dice...

(tunggu 2 detik)

5
```

---

# Alur Program Dice Simulator

```
Program Dimulai

↓

Pengguna menekan Enter

↓

Loading...

↓

Program menunggu 2 detik

↓

Menghasilkan angka acak 1-6

↓

Menampilkan hasil dadu

↓

Program selesai
```

---

# Project Hari Ini

## Dice Simulator

Buat program simulasi lempar dadu.

Langkah-langkah:

1. Import `random`
2. Import `time`
3. Tampilkan tulisan

```
Rolling Dice...
```

4. Tunggu selama 2 detik.
5. Tampilkan angka acak dari 1 sampai 6.

Contoh

```
Rolling Dice...

🎲 Hasil Dadu : 4
```

---

# Pengembangan Project

Tambahkan tampilan seperti berikut.

```
=========================
      DICE SIMULATOR
=========================

Rolling...

🎲
🎲
🎲

Hasil Dadu : 6

=========================
```

Gunakan `time.sleep()` agar animasi terasa lebih nyata.

---

# Challenge 1

Buat dua buah dadu.

Contoh

```
Dadu 1 : 5

Dadu 2 : 3

Total : 8
```

---

# Challenge 2

Buat permainan sederhana.

Aturan:

Jika hasil dadu

```
6
```

Maka tampilkan

```
Jackpot!
```

Jika selain 6

```
Coba Lagi!
```

---

# Challenge 3

Gunakan `os.system("cls")` agar layar dibersihkan sebelum hasil akhir ditampilkan.

Contoh

```
Rolling...

(terminal dibersihkan)

====================
HASIL DADU

🎲 5

====================
```

---

# Mini Challenge

Buat simulator acak lainnya.

Contoh:

- Lempar Koin
- Batu Gunting Kertas
- Lucky Number
- Spin Wheel
- Tebak Warna
- Gacha Item
- Lucky Box

Gunakan minimal satu library yang telah dipelajari.

---

# Kesalahan yang Sering Terjadi

❌ Lupa mengimpor library

```python
print(random.randint(1,6))
```

Error karena belum menulis

```python
import random
```

---

❌ Salah menulis nama library

```python
Random.randint()
```

Python membedakan huruf besar dan kecil.

Yang benar

```python
random.randint()
```

---

❌ Salah menentukan batas angka

```python
random.randint(6,1)
```

Harus dimulai dari angka yang lebih kecil.

```python
random.randint(1,6)
```

---

❌ Lupa memberi tanda kurung pada `sleep()`

```python
time.sleep
```

Yang benar

```python
time.sleep(2)
```

---

# Ringkasan

Hari ini kita telah belajar:

✅ Apa itu Library

✅ Perintah `import`

✅ Library `random`

✅ `random.randint()`

✅ Library `time`

✅ `time.sleep()`

✅ Library `os`

✅ `os.system()`

✅ Menggunakan beberapa library sekaligus

✅ Membuat Dice Simulator

---

# Persiapan Pertemuan Selanjutnya

Pada pertemuan berikutnya kita akan belajar:

- Operator Aritmatika
- Operator Assignment
- Operator Comparison
- Operator Logical
- Menggunakan operator dalam program
- Project: Kasir Sederhana
