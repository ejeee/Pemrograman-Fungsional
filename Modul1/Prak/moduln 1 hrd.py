# Inisialisasi daftar buku yang tersedia
buku_tersedia = []

# Inisialisasi daftar buku yang dipinjam oleh pengguna
buku_dipinjam = []

# Fungsi untuk menambahkan buku oleh admin
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    buku_tersedia.append({"Judul": judul, "Penulis": penulis})
    print("Buku '{}' telah ditambahkan.".format(judul))

# Fungsi untuk menampilkan buku yang tersedia
def tampilkan_buku_tersedia():
    print("\nBuku yang tersedia:")
    for index, buku in enumerate(buku_tersedia):
        print("{}. Judul: {}, Penulis: {}".format(index + 1, buku["Judul"], buku["Penulis"]))

# Fungsi untuk melakukan peminjaman buku oleh pengguna
def pinjam_buku(user):
    tampilkan_buku_tersedia()
    nomor_buku = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1

    if nomor_buku >= 0 and nomor_buku < len(buku_tersedia):
        buku = buku_tersedia.pop(nomor_buku)
        buku_dipinjam.append({"Judul": buku["Judul"], "Penulis": buku["Penulis"], "Peminjam": user})
        print("Anda telah meminjam buku '{}'.".format(buku["Judul"]))
    else:
        print("Nomor buku tidak valid.")

# Fungsi untuk mengembalikan buku oleh pengguna
def kembalikan_buku(user):
    print("\nBuku yang Anda pinjam:")
    for index, buku in enumerate(buku_dipinjam):
        if buku["Peminjam"] == user:
            print("{}. Judul: {}, Penulis: {}".format(index + 1, buku["Judul"], buku["Penulis"]))

    nomor_buku = int(input("Masukkan nomor buku yang ingin dikembalikan: ")) - 1

    if nomor_buku >= 0 and nomor_buku < len(buku_dipinjam):
        buku = buku_dipinjam.pop(nomor_buku)
        buku_tersedia.append({"Judul": buku["Judul"], "Penulis": buku["Penulis"]})
        print("Anda telah mengembalikan buku '{}'.".format(buku["Judul"]))
    else:
        print("Nomor buku tidak valid.")

# Fungsi utama
def main():
    while True:
        print("\nPilihan Menu:")
        print("1. Admin - Input Buku")
        print("2. User - Pinjam Buku")
        print("3. User - Kembalikan Buku")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            username = input("Masukkan nama pengguna (user): ")
            pinjam_buku(username)
        elif pilihan == "3":
            username = input("Masukkan nama pengguna (user): ")
            kembalikan_buku(username)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
