# Введіть рахунок першого тайму: 1:4
# Введіть рахунок другого тайму: 2:1
# Програма має видати підсумковий рахунок, тобто 3:5
first_half = input("Enter scores of the first half: ")
second_half = input("Enter scores of the second half:")

colon_index = first_half.index(":")
colon_index_2 = second_half.index(":")

first_half_1 = int(first_half[0])
first_half_2 = int(first_half[colon_index + 1:])

second_half_1 = int(second_half[0])
second_half_2 = int(second_half[colon_index_2 + 1:])

print(f"{first_half_1 + second_half_1} : {first_half_2 + second_half_2}")
