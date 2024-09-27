a = int(input("Пробег за день:"))
b = int(input("Пробег всего:"))
y = 1
while a < b:
    a = a + a/10
    y += 1
print (f"Номер дня = {y}")
