dollar = 40.25
money = input("Enter values of money: ")

parts = money.split()
currency = parts[1]
value = int(parts[0])


if currency == "грн":
    print(f"{round(value / dollar, 2)} $")
    print(f"{value / dollar:6.2f} $")
else:
    print(f"{value * dollar} грн")




