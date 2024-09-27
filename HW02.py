seconds = int(input("Введите время в секундах:"))
hour = seconds // 3600
decimal = seconds % 3600
minute = decimal // 60
second = decimal % 60
print(f"{hour}:{minute}:{second}")








