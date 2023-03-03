# Який час буде на годиннику (ГГ:ХХ),
# якщо введено кількість хвилин, які пройшли з початку доби

minutes_since_start = int(input("Enter minutes since the day has started: "))
current_time = float(minutes_since_start / 60)
# print(str(current_time))
new_current_time = str(current_time)
dot_index = new_current_time.index(".")
hours_index = int(minutes_since_start[:dot_index])
minutes_index = int(minutes_since_start[dot_index+1:])

if hours_index < 10:
    print(f"It's 0{hours_index} : {minutes_index}")
elif hours_index <= 23:
    print(f"It's {hours_index} : {minutes_index}")
elif hours_index == 24:
    print(f"It's 00 : {minutes_index}")
