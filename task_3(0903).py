dollar = 40.25
number_of_el = int(input("Enter the number of value you want to convert: "))

for element in range(number_of_el):
    money = input("Enter the value you want to convert: ")
    parts = money.split()
    currency = parts[1]
    value = int(parts[0])
    if currency == 'грн':
        print(f"{round(value / dollar, 2)} $")
        # print(f"{value / dollar:6.2f} $")
    else:
        print(f"{value * dollar} грн")