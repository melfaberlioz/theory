# Визначити, скільки хвилин пройшло з початку
# доби за введеним часом у форматі ГГ:ХХ

time = input("Enter time in format HH:MM: ")
colon_index = time.index(":")
hours = int(time[:colon_index])
minutes = int(time[colon_index+1:])

print(f"here is {hours * 60 + minutes} minutes since the day has started.")
