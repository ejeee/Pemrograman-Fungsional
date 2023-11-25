def perkalian(a):
    def kali(b):
        return a * b
    return kali

#HoF penggunaan fungsi nilai/argumen
def return_hof():
    result = perkalian(2)(9)
    print("\nHasil perkalian HOF: ", result)
return_hof()

#currying transformasi fungsi 
def return_currying():
    kali = perkalian (2)
    result = kali(9)
    print("Hasil perkalian currying: ", result)
    print("\n")
return_currying()

