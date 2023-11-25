# Fungsi penambahan
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan 0"
    return a / b

# Contoh penggunaan fungsi-fungsi ini:
angka1 = 10
angka2 = 5

hasil_penambahan = add(angka1, angka2)
hasil_pengurangan = minus(angka1, angka2)
hasil_perkalian = mult(angka1, angka2)
hasil_pembagian = div(angka1, angka2)

print(f"Hasil Penambahan: {hasil_penambahan}")
print(f"Hasil Pengurangan: {hasil_pengurangan}")
print(f"Hasil Perkalian: {hasil_perkalian}")
print(f"Hasil Pembagian: {hasil_pembagian}")
