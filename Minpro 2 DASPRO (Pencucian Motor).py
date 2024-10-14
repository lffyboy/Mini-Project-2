#Membuat program jasa layanan dan transaksi pada pencucian motor yang terdapat admin dan pembeli

# Data Paket Layanan dan Transaksi Pencucian Motor Lutpi CleaningFasttt!
layanan = [
    {"nama": "Cuci Motor Biasa", "harga": 12000},
    {"nama": "Cuci Motor Tanpa Sentuh", "harga": 18000},
    {"nama": "Cuci Motor + Semir Ban", "harga": 22000},
    {"nama": "Cuci Motor + Wax Body", "harga": 27000},
    {"nama": "Cuci Motor Paket Lengkap (Body, Semir Ban, Wax Body)", "harga": 30000}
]

from prettytable import PrettyTable

# Data pengguna login
users = {
    "lutpi": "lutpi11",
    "celsi": "celsi12"
}

def login():
    print("[^ ^] Login [^ ^]")
    username = input("Username: ")
    password = input("Password: ")

# Memeriksa info login
    if username in users and users[username] == password:
        return username
    else:
        print("Username atau password salah!")
        return None

def menu_admin():
    while True:
        print("[^ ^] Menu Admin [^ ^]")
        print("1. Tambah Paket")
        print("2. Lihat Paket")
        print("3. Update Paket")
        print("4. Hapus Paket")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            tambah_paket()
        elif pilihan == '2':
            lihat_paket()
        elif pilihan == '3':
            update_paket()
        elif pilihan == '4':
            hapus_paket()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")

def menu_pembeli():
    while True:
        print("\n[^ ^] Menu Pembeli [^ ^]")
        print("1. Lihat Paket Pencucian")
        print("2. Pilih Paket Pencucian")
        print("3. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            lihat_paket()
        elif pilihan == '2':
            pilih_paket()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!")

def tambah_paket():
    nama = input("Nama paket pencucian: ")
    harga = float(input("Harga paket pencucian: "))
    layanan.append({"nama": nama, "harga": harga}) 
    print("Paket pencucian berhasil ditambahkan!")

def lihat_paket():
    if not layanan:
        print("Belum ada paket pencucian tersedia.")
    else:
        from prettytable import PrettyTable
        
        tabel = PrettyTable()
        tabel.title = "PAKET Lutpi CleaningFasttt!"
        tabel.field_names = ["No", "Jenis Paket", "Harga (Rp)"]
        for pkt, l in enumerate(layanan, 1):
            tabel.add_row([pkt, l["nama"], f"Rp{l['harga']}"])
        print(tabel)

def update_paket():
    lihat_paket()
    paket = int(input("Pilih nomor paket yang ingin diubah: ")) - 1
    if 0 <= paket < len(layanan):
        layanan[paket]['nama'] = input("Nama baru: ")
        layanan[paket]['harga'] = float(input("Harga baru: "))
        print("Paket pencucian berhasil diubah!")
    else:
        print("Layanan tidak ditemukan!")

def hapus_paket():
    lihat_paket()
    paket = int(input("Pilih nomor paket yang ingin dihapus: ")) - 1
    if 0 <= paket < len(layanan):
        layanan.pop(paket)
        print("Paket pencucian berhasil dihapus!")
    else:
        print("Paket tidak ditemukan!")

def pilih_paket():
    lihat_paket()
    paket = int(input("Pilih nomor paket yang ingin dipilih: ")) - 1
    if 0 <= paket < len(layanan):
        jumlah = int(input("Masukkan jumlah kendaraan: "))
        total = layanan[paket]['harga'] * jumlah
        print(f"Total biaya pencucian: Rp{total}")
    else:
        print("Paket tidak ditemukan!")

def main():
    print("Selamat datang di Pencucian Motor Lutpi CleaningFasttt!")
    user_role = login()

    if user_role == 'lutpi':
        menu_admin()
    elif user_role == 'celsi':
        menu_pembeli()
    else:
        print("Akses ditolak. Silakan coba lagi.")

if __name__ == "__main__":
    main()



