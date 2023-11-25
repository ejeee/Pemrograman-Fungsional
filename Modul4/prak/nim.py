import math

#translasi
def translate(tx, ty):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            new_x = x + tx
            new_y = y + ty
            return func((new_x, new_y), m)

        return wrapper

    return decorator

#dilatasi
def scale(sx, sy):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            new_x = x * sx
            new_y = y * sy
            return func((new_x, new_y), m)

        return wrapper

    return decorator

#rotasi
def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            t = math.radians(angle)
            new_x = x * math.cos(t) - y * math.sin(t)
            new_y = x * math.sin(t) + y * math.cos(t)
            return func((new_x, new_y), m)

        return wrapper

    return decorator


y_intercept = lambda p, m: p[1] - m * p[0]


if __name__ == "__main__":

    # syarat modul:
    # 3 digit NIM terakhir [xyz]
    # titik A (x,y); gradien = x; tx = y; ty = z; sx = z; sy = x
    # 5, 0, 3 = x, y, z
    # A (5, 0) | m = 5
    # tx = 0 | ty = 3
    # sx = 3 | sy = 5

    while True:
        nim = str(input("\nMasukkan 3 digit terakhir NIM: "))

        if len(nim) == 3:
            x, y, z = map(int, nim)
        else:
            print("Harus 3 digit")
            continue

        point = (x, y)
        m = z
        tx, ty = y, z
        sx, sy = z, x

        def line_equation_of(point, m):
            c = y_intercept(point, m)
            return f"y = {m:.2f}x + {c:.2f}"

        @translate(tx, ty)
        @rotate(60)
        @scale(sx, sy)
        def eq_after_transformation(point, m):
            c = y_intercept(point, m)
            return f"y = {m:.2f}x + {c:.2f}"

        print(f"Persamaan garis yang melalui titik {point} dan bergradien {m}:")
        print(line_equation_of(point, m))

        print(f"Persamaan garis baru setelah ditransformasi:")
        print(eq_after_transformation(point, m))
        print(" ")

        break