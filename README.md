### PROJECT UAS
| Variable | Isi |
| -------- | --- |
| Nama | Via Nirmala Mahdalena  |
| NIM | 312310484 |
| Kelas | TI.23.A5 |
| Mata Kuliah | Bahasa Pemrograman |

Buatlah program kasir di sebuah kantin, dengan kondisi berikut:

* List opsi pilihan makanan/minuman dan aksi, bisa menggunakan
format dictionary
* Program harus meminta input pilihan makanan dari pengguna.
* Program harus menghitung total harga makanan yang dipesan.
* Program harus menampilkan struk pembelian.
### Program tersebut merupakan program sederhana untuk melakukan transaksi pembelian makanan atau minuman di sebuah warung. Berikut adalah penjelasan dari setiap bagian program:
Definisi Menu:
```python
menu = {

    "Cilok": 7000,
    "Cireng Ayam Suwir": 10000,
    "Citul Ayam Suwir": 12000,
    "Cibay Ayam": 11000,
    "Cimol Bojot": 5000,
}
```
Program ini mendefinisikan daftar menu makanan/minuman beserta harganya dalam bentuk kamus (dictionary).

### Inisialisasi List Pesanan:
```python
pesanan = []
```
Program menginisialisasi list pesanan di luar loop while yang akan digunakan untuk menyimpan pilihan menu yang dipilih oleh pengguna.

### Mulai Transaksi:
```python
print("Selamat datang di warung kita!")
```
Program memberikan sambutan kepada pengguna.

### Loop Input Pengguna:
```python
while True:
    # ...
```
Program memulai loop tak terbatas yang meminta pengguna untuk memilih menu makanan/minuman hingga pengguna memasukkan 's' untuk selesai.

### Tampilan Menu dan Input Pengguna:
``` python

for key, value in menu.items():
    print(f"{key}: Rp{value}")
pilihan = input("Masukkan pilihan Anda (tekan s untuk selesai): ")
```
Program menampilkan opsi menu kepada pengguna dan meminta input pilihan. Jika pengguna memasukkan 's', loop akan berhenti.

### Validasi Pilihan Pengguna:
```python

if pilihan not in menu:
    print("Pilihan Anda tidak valid. Silakan pilih kembali.")
    continue
```
Jika pilihan pengguna tidak valid (tidak ada dalam daftar menu), program memberikan pesan kesalahan dan meminta input ulang.

### Penambahan Menu ke Pesanan:
```python
pesanan.append(pilihan)
```
Program menambahkan menu yang dipilih oleh pengguna ke dalam list pesanan.

### Hitung Total Harga Pesanan:
```python
total_harga = sum(menu[menu_item] for menu_item in pesanan)
```
Program menghitung total harga pesanan dengan menjumlahkan harga setiap menu yang ada dalam list pesanan.

### Tampilkan Struk Pembelian:
```python
# ...
```
Program menampilkan struk pembelian berisi detail setiap menu yang dipilih oleh pengguna dan total harga pembelian.
# TERIMAKASIH
