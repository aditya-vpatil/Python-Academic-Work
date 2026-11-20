''' Quiz Application '''

questions = [
    ("What is 2 + 2? ", "4"),
    ("Which keyword starts a loop over a range? ", "for"),
    ("What is the result of 5 * 3? ", "15"),
    ("Which data type stores True or False? ", "bool"),
    ("Which keyword repeats while a condition is true? ", "while")
]
score = 0
for question, answer in questions:
    user_answer = input(question).strip().lower()
    if user_answer == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect. Correct answer:", answer)
percentage = (score / len(questions)) * 100
print("Score:", score, "out of", len(questions))
print("Percentage:", percentage, "%")
if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good")
else:
    print("Keep Practicing")