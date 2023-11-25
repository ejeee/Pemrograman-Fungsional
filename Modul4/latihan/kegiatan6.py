#NIM ganjil
def point(x, y):
    return x, y

def line_equation_of(x1, y1, M):
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (5,0) dan bergradien 3:")
print(line_equation_of(5, 0, 3))#nilai input 3 digit NIM akhir 503