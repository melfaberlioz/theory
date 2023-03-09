# Який час буде на годиннику (ГГ:ХХ),
# якщо введено кількість хвилин, які пройшли з початку доби

def repr_time(value):
    if value < 10:
        return '0' + value
    return str(value)

minutes_since_start = int(input("Enter minutes since the day has started: "))
hours = minutes_since_start // 60
minutes = minutes_since_start % 60

# repr_h = str(hours)
# repr_m = str(minutes)
# if hours < 10:
#     repr_h  = '0' + repr_h
# if minutes < 10:
#     repr_m = '0' + repr_m

print(f"{repr_time(hours)}:{repr_time(minutes)}")
