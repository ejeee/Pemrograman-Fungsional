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

# Struktur pohon
def tree(expression):
    if isinstance(expression, tuple):
        left, operation, right = expression
        if operation == "+":
            return add(tree(left), tree(right))
        elif operation == "-":
            return minus(tree(left), tree(right))
        elif operation == "*":
            return mult(tree(left), tree(right))
        elif operation == "/":
            return div(tree(left), tree(right))
        else:
            return "Operasi tidak valid"
    else:
        return expression

# Contoh pohon ekspresi: (2+3) * (5-1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
