# Визначити тип введеного речення
# (розповідне, питальне, окличне, неможливо визначити)

sentence = input("Enter sentence: ")
punctuation = sentence[-1]

if punctuation == "." or sentence == "...":
    print("The sentence is a declarative sentence.")
elif punctuation == "?":
    print("The sentence is an interrogative sentence.")
elif punctuation == "!":
    print("The sentence is an exclamatory sentence.")
else:
    print("It's impossible to define the type.")