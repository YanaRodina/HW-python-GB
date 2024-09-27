number: str = input("Введите любое целое положительное число:")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
        print(x)
