num = int(input('masukkkan sebuah bilangan:'))
def tipe(num):
    if num == 0:
        print(f"{num} merupakan bilangan nol")
    elif num % 2 != 0: 
        print(f"{num} merupakan bilangan ganjil")
    else:
        print(f"{num} merupakan bilangan genap")
    hasil = num*(num+1)
    return hasil
hasil = tipe(num)
print(f"hasil perkalian bilangan dengan bilangan setelahnya adalah: {hasil}")
