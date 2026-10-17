# ---------------------------------------
# Program 119: Quiz Application
# Description: Conducts a simple multiple-choice quiz.
# Author: Anugya Agrawal
# ---------------------------------------

score = 0

questions = [
    ("What is the capital of India?", "Delhi"),
    ("How many days are there in a week?", "7"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is 5 + 5?", "10"),
    ("Which language is used to create this program?", "Python")
]

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", answer)

print("\nQuiz Completed!")
print("Your Score:", score, "/", len(questions))
