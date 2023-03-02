# Визначити переможця за введеним рахунком.
# Наприклад, 3:1 - перемогли господарі,
# 3:3 - нічия,
# 2:12 - перемогли гості

scores = input("Enter scores: ")

colon_index = scores.index(":")
host_score = int(scores[:colon_index])
guests_score = int(scores[colon_index + 1:])

if host_score > guests_score:
    print("The host is the winner. Congratulations!")
elif host_score < guests_score:
    print("The guests are winners. Congratulations!")
else:
    print("It's a draw. Thank you for taking part in our match!")