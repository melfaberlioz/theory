# Програма приймає час у 24-годинному форматі, а повертає у 12-годинному.

from datetime import datetime
time_24 = input("Введіть час у 24-годинному форматі: ")
t = datetime.strptime(time_24, "%H:%M")
time_12 = t.strftime("%I:%M %p")
print(f"Час у 12-годинному форматі: {time_12}")

# strptime() method creates a datetime object from a given str
# strftime() method takes one or more format codes and returns
# a formatted string based on it. Here is format codes:
# %H - hours
# %M - minutes
# %I - hour(12-hour clock)
# %p - AM or PM
# %M - minutes

colon_index = time_24.index(':')
hours_24 = int(time_24[:colon_index])

if hours_24 > 12:
    hours_12 = hours_24-12
else:
    hours_12 = hours_24

print(f"{hours_12 + time_24[colon_index:]}")

