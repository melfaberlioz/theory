person = input("Введіть особу: ")

gap = person.index(' ')
# new_lastname = person[gap+1] + ". " + person[:gap]
print(f"{person[gap+1]}. {person[:gap]}")
