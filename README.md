# labpy06

# BIODATA

# Nama   : LOLA SEFTYLIANI
# Kelas  : TI.24.A.4
# NIM    : 312410339
# Matkul : Bahasa Pemograman 

## Latihan 1
![Screenshot 2024-12-01 120018](https://github.com/user-attachments/assets/a2058a1c-acba-453b-8ba7-7f6334ba071b)

## Latihan 1.py

```python
import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args) if args else 0
d = lambda s: "".join(set(s))

print("lambda a(5):", a(5))
print("lambda b(3, 4):", b(3, 4))
print("lambda c(1, 2, 3, 4, 5):", c(1, 2, 3, 4, 5))
print("lambda d('hello lola'):", d("lola"))
```

## code program tersebut
![code](https://github.com/user-attachments/assets/e072b90b-e78c-4fbc-8abb-eb8a625659e3)

## Hasil program tersebut
![Screenshot 2024-12-01 220559](https://github.com/user-attachments/assets/9e8c6f4b-9103-4141-b396-327312638272)

## Tugas Praktikum
![Screenshot 2024-12-01 220842](https://github.com/user-attachments/assets/cccb40dd-9a46-4ead-93b6-b5522e96582c)

## Tugas Praktikum.py

```python
data_mahasiswa = []

def tambah():
    print("-" * 42)
    nama = input("1. Masukkan nama mahasiswa: ")
    nilai = float(input("2. Masukkan nilai mahasiswa: "))
    print("-" * 42)
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("=" * 42)
    print("|    --- Data berhasil ditambahkan! ---  |")
    print("=" * 42)

def tampilkan():
    if not data_mahasiswa:
        print()
        print("=" * 34)
        print("--- Belum ada data mahasiswa ---")
        print("=" * 34)
    else:
        print()
        print("--- Daftar Nilai Mahasiswa A.4 ---")
        print("=" * 34)
        print("| NO |       NAMA       | NILAI |")
        print("-" * 33)
        for i, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"|{i:3}.| {mahasiswa['nama']:16} | {mahasiswa['nilai']:6}|")
        print("=" * 34)

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'] != nama]
    print("=" * 65)
    print(f"--- Data mahasiswa dengan nama '{nama}' telah dihapus! ---")
    print("=" * 65)

def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = float(input(f"2. Masukkan nilai baru untuk {nama}: "))
            print("-" * 55)
            print("=" * 55)
            print("|            --- Data berhasil diubah! ---            |")
            print("=" * 55)
            return
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

daftar_mahasiswa = {}

def menu():
    while True:
        print()
        print("=" * 20)
        print("|   --- MENU ---   |")
        print("=" * 20)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        print()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            print()
            print("-" * 65)
            nama = input("1. Masukkan nama mahasiswa yang ingin dihapus: ")
            print("-" * 65)
            hapus(nama)
        elif pilihan == "4":
            print()
            print("-" * 55)
            nama = input("1. Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print()
            print("=" * 42)
            print("| --- Program selesai. Terima kasih! --- |")
            print("=" * 42)
            print()
            break
        else:
            print()
            print("=" * 51)
            print("| --- Pilihan tidak valid. Silakan coba lagi! --- |")
            print("=" * 51)

menu()
```
## Penjelasan Code

```python
data_mahasiswa = []

def tambah():
    print("-" * 42)
    nama = input("1. Masukkan nama mahasiswa: ")
    nilai = float(input("2. Masukkan nilai mahasiswa: "))
    print("-" * 42)
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("=" * 42)
    print("|    --- Data berhasil ditambahkan! ---  |")
    print("=" * 42)
```

Meminta pengguna untuk memasukkan nama mahasiswa. Jika nama kosong (hanya spasi), program akan mencetak pesan kesalahan dan keluar dari fungsi, menggunakan try-except untuk mencoba mengonversi nilai yang dimasukkan menjadi integer. Jika gagal, program mencetak pesan kesalahan, jika semua input valid, data mahasiswa (nama dan nilai) ditambahkan ke dalam dictionary `daftar_mahasiswa`, dan program mencetak pesan konfirmasi.

```python
def tampilkan():
    if not data_mahasiswa:
        print()
        print("=" * 34)
        print("--- Belum ada data mahasiswa ---")
        print("=" * 34)
    else:
        print()
        print("--- Daftar Nilai Mahasiswa A.4 ---")
        print("=" * 34)
        print("| NO |       NAMA       | NILAI |")
        print("-" * 33)
        for i, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"|{i:3}.| {mahasiswa['nama']:16} | {mahasiswa['nilai']:6}|")
        print("=" * 34)
```

Fungsi ini menampilkan semua data mahasiswa yang ada dalam `daftar_mahasiswa` kosong, Jika tidak kosong, mencetak "Daftar Mahasiswa:" dan menggunakan loop untuk mencetak setiap nama mahasiswa dan nilai mereka dalam format `nama: nilai`.

```python
def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'] != nama]
    print("=" * 65)
    print(f"--- Data mahasiswa dengan nama '{nama}' telah dihapus! ---")
    print("=" * 65)
```

Memeriksa apakah nama mahasiswa yang ingin dihapus ada dalam `daftar_mahasiswa`. Jika ada, data mahasiswa dihapus menggunakan `del`, dan mencetak pesan konfirmasi bahwa data berhasil dihapus. Jika tidak ada, mencetak pesan bahwa mahasiswa tersebut tidak ditemukan.

```python
def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = float(input(f"2. Masukkan nilai baru untuk {nama}: "))
            print("-" * 55)
            print("=" * 55)
            print("|            --- Data berhasil diubah! ---            |")
            print("=" * 55)
            return
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")
```

Mengubah nilai mahasiswa berdasarkan nama yang diberikan, Memeriksa apakah nama mahasiswa ada dalam `daftar_mahasiswa`. Jika ada, meminta pengguna untuk memasukkan nilai baru dan mencoba mengonversinya menjadi `integer`. Jika konversi berhasil, nilai mahasiswa diperbarui dalam `dictionary`, dan mencetak pesan konfirmasi, Jika konversi gagal, mencetak pesan kesalahan. Jika nama tidak ditemukan, mencetak pesan bahwa mahasiswa tersebut tidak ditemukan.

```python
daftar_mahasiswa = {}
```

`daftar_mahasiswa` adalah `dictionary` kosong yang akan digunakan untuk menyimpan data mahasiswa, dengan nama sebagai kunci dan nilai sebagai nilai.

```python
def menu():
    while True:
```

Fungsi utama `def menu()` yang menjalankan program, menampilkan menu pilihan,menggunakan loop while untuk terus menampilkan menu. `while True` loop tak terbatas yang akan terus berjalan sampai perintah break dijalankan.

```python
  print()
        print("=" * 20)
        print("|   --- MENU ---   |")
        print("=" * 20)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        print()
```

Program mencetak menu dengan lima opsi yang dapat dipilih pengguna tersebut:

1. Tambah data: untuk menambahkan data mahasiswa baru
2. Tampilkan data: untuk menampilkan semua data mahasiswa yang telah dimasukkan
3. Hapus data: Menghapus data mahasiswa berdasarkan nama
4. Ubah data: Mengubah nilai mahasiswa berdasarkan nama
5. Keluar: Keluar dari program

```python
 pilihan = input("Pilih menu (1-5): ")
```

Program meminta `input` dari pengguna untuk memilih salah satu menu (1-5).

```python
 if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
```

Jika pengguna memilih 1, maka fungsi akan `tambah()`, Jika pengguna memilih 2, maka fungsi akan `tampilkan()` untuk menampilkan semua data mahasiswa yang ada dalam `daftar_mahasiswa`

```python
 elif pilihan == "3":
            print()
            print("-" * 65)
            nama = input("1. Masukkan nama mahasiswa yang ingin dihapus: ")
            print("-" * 65)
            hapus(nama)
        elif pilihan == "4":
            print()
            print("-" * 55)
            nama = input("1. Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
```
jika pengguna memilih 3, program akan meminta `input` nama mahasiswa yang ingin dihapus, Jika pengguna memilih 4, program akan meminta `input` nama mahasiswa yang ingin diubah.

```python
  elif pilihan == "5":
            print()
            print("=" * 42)
            print("| --- Program selesai. Terima kasih! --- |")
            print("=" * 42)
            print()
            break
```

Jika pengguna memilih 5, program akan mencetak pesan `"Terima kasih!"` dan keluar dari loop utama dengan menggunakan break.

```python
else:
            print()
            print("=" * 51)
            print("| --- Pilihan tidak valid. Silakan coba lagi! --- |")
            print("=" * 51)
```

Jika pengguna memasukkan pilihan selain angka `1 hingga 5`, program akan menampilkan pesan `"Pilihan tidak valid."` dan kembali menampilkan menu.

## Code Prpgram tersebut:
![code 22](https://github.com/user-attachments/assets/c92657ff-3298-4f77-a9bc-56c88a92715d)

## Hasil program tersebut:
![Screenshot 2024-12-01 192528](https://github.com/user-attachments/assets/c801b598-cbb0-44a1-a771-b035e5ebb9ab)

![Screenshot 2024-12-01 192550](https://github.com/user-attachments/assets/ed394ceb-ab2e-4067-88f8-559bd53d3dc7)

![Screenshot 2024-12-01 192636](https://github.com/user-attachments/assets/2ef1a03c-2093-4545-af4b-2945b54342da)

![Screenshot 2024-12-01 192705](https://github.com/user-attachments/assets/5f511543-6e46-457d-9089-9499cd954002)

![Screenshot 2024-12-01 231841](https://github.com/user-attachments/assets/611ae32b-0444-4dba-805b-d6267f86dae5)

## Hasil flowchart code tersebut:


















