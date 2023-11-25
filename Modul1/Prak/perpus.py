class Buku:
    def __init__(self, judul, penulis, tersedia=True):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = tersedia

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Sedang Dipinjam"
        return f"'{self.judul}' oleh {self.penulis} ({status})"


class Akun:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Admin(Akun):

    def input_buku(self):
        judul = input("Judul buku: ")
        penulis = input("Penulis buku: ")
        buku = Buku(judul, penulis)
        daftar_buku.append(buku)
        print(f"Buku '{judul}' oleh {penulis} telah ditambahkan.")


class User(Akun):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.buku_dipinjam = []

    def pinjam_buku(self):
        judul = input("Judul buku yang ingin dipinjam: ")
        for buku in daftar_buku:
            if buku.judul == judul and buku.tersedia:
                buku.tersedia = False
                self.buku_dipinjam.append(buku)
                print(f"Anda berhasil meminjam buku '{judul}'.")
                return
        print(f"Buku '{judul}' tidak tersedia.")

    def kembalikan_buku(self):
        judul = input("Judul buku yang ingin dikembalikan: ")
        for buku in self.buku_dipinjam:
            if buku.judul == judul:
                buku.tersedia = True
                self.buku_dipinjam.remove(buku)
                print(f"Anda telah mengembalikan buku '{judul}'.")
                return
        print(f"Anda tidak meminjam buku dengan judul '{judul}'.")


daftar_buku = []

def main():
    print("Selamat datang di Perpustakaan UMM!")
    while True:
        print("\nMenu:")
        print("1. Login Admin")
        print("2. Login User")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            admin_menu()
        elif pilihan == "2":
            user_menu()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")


def admin_menu():
    username = input("Username Admin: ")
    password = input("Password Admin: ")

    if username == "admin" and password == "admin123":
        admin = Admin(username, password)
        while True:
            print("\nMenu:")
            print("1. Input Buku Baru")
            print("2. Daftar Buku")
            print("3. Kembali ke Menu Utama")
            pilihan = input("Masukkan pilihan: ")

            if pilihan == "1":
                admin.input_buku()
            elif pilihan == "2":
                lihat_daftar_buku()
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid!")
    else:
        print("Username atau password salah!")


def user_menu():
    username = input("Username User: ")
    password = input("Password User: ")

    user = User(username, password)
    while True:
        print("\nMenu:")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Daftar Buku")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            user.pinjam_buku()
        elif pilihan == "2":
            user.kembalikan_buku()
        elif pilihan == "3":
            lihat_daftar_buku()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")


def lihat_daftar_buku():
    buku_dipinjam = sum(1 for buku in daftar_buku if not buku.tersedia)
    if not daftar_buku:
        print("Belum ada buku yang ditambahkan.")
    elif buku_dipinjam == len(daftar_buku):
        print("Semua buku telah dipinjam.")
    else:
        print("\nDaftar Buku Tersedia:")
        for buku in daftar_buku:
            if buku.tersedia:
                print(buku)



if __name__ == "__main__":
    main()
