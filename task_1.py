person = input("Введіть особу: ")

gap = person.index(' ') + 1
new_lastname = person[:gap] + person[gap:-5] + "."
print(new_lastname)