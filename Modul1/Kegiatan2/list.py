random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
str_list = []

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan untuk integer
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {"Ratusan": ratusan, "Puluhan": puluhan, "Satuan": satuan}
    elif isinstance(item, float):
        # Menambahkan float ke dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menambahkan string ke dalam list
        str_list.append(item)

print("Data Integer (dalam dictionary):")
print(int_dict)

print("Data Float (dalam tuple):")
print(float_tuple)

print("Data String (dalam list):")
print(str_list)
