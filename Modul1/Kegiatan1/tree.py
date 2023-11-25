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

# Kombinasi fungsi tree
def tree(operation, left, right):
    if operation == "+":
        return add(left, right)
    elif operation == "-":
        return minus(left, right)
    elif operation == "*":
        return mult(left, right)
    elif operation == "/":
        return div(left, right)
    else:
        return "Operasi tidak valid"

hasil = tree("+", 10, tree("*", 5, 2))  # Hasilnya adalah 10 + (5 * 2) = 20
print(f"Hasil Operasi: {hasil}")
