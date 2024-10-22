import math
text = input("Input Text: ")
length = text.count("")
count = len(text.split())

words = len(text.split())
comma_count = text.count(",")
space_count = text.count(" ")
period_count = text.count(".")
exclamation_count = text.count("!")
question_count = text.count("?")
sentecens = period_count + exclamation_count + question_count
letters = len(text)-comma_count-sentecens-space_count-text.count("'y")

L = letters / words * 100
S = sentecens / words * 100
index = round((0.0588 * L) - (0.296 * S) - 15.8)
if index == 16 or index > 16:
    print("Grade 16+")

elif index <= 1:

    print("Before Grade 1")

else:
    print(f"Grade {index}")
