# Definisikan daftar opsi pilihan makanan/minuman dan harga
menu = {
    "Cilok": 7000,
    "Cireng Ayam Suwir": 10000,
    "Citul Ayam Suwir": 12000,
    "Cibay Ayam": 11000,
    "Cimol Bojot": 5000,
}

# Inisialisasi list pesanan di luar loop while
pesanan = []

# Mulai transaksi
print("Selamat datang di warung kita!")

# Permintaan input pilihan makanan dari pengguna
while True:
    print("Pilih menu makanan/minuman yang ingin Anda pesan:")
    for key, value in menu.items():
        print(f"{key}: Rp{value}")

    pilihan = input("Masukkan pilihan Anda (tekan q untuk selesai): ")

    # Jika pilihan pengguna adalah q, maka hentikan transaksi
    if pilihan == "q":
        break

    # Jika pilihan pengguna tidak valid, maka minta input ulang
    if pilihan not in menu:
        print("Pilihan Anda tidak valid. Silakan pilih kembali.")
        continue

    # Menambahkan menu yang dipilih ke dalam list pesanan
    pesanan.append(pilihan)

# Hitung total harga pesanan
total_harga = sum(menu[menu_item] for menu_item in pesanan)

# Tampilkan struk pembelian
print("--------------------------------------------------")
print("Struk Pembelian Kantin")
print("--------------------------------------------------")
print("No. | Menu | Harga")
print("-----|------|------")
for i, menu_item in enumerate(pesanan):
    print(f"{i + 1} | {menu_item} | Rp{menu[menu_item]}")
print("--------------------------------------------------")
print(f"Total Harga: Rp{total_harga}")
print("--------------------------------------------------")