dollar = 40.25
money = input("Enter value of money: ")


# space_index = money.index(" ")
# currency = money[space_index + 1:]
# value = int(money[:space_index])
#
# if currency == "грн":
#     print(f"{round(value / dollar, 2)} $")
#     print(f"{value / dollar:6.2f} $")
# else:
#     print(f"{value * dollar} грн")

parts = money.split()
currency = parts[1]
value = int(parts[0])

if currency == "грн":
    #print(f"{round(value / dollar, 2)} $")
    print(f"{value / dollar:6.2f} $")
else:
    print(f"{value * dollar} грн")



