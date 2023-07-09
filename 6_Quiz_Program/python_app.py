# A dictionary that stores questions and answers
# Have a variable that tracks the score of the player
# Loop through the dictionary using the key values pairs
# Display each question to the user and allow them to answer
# Tell them if they are right or wrong
# Show the final result when Quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    "question2": {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "answer": "Japan"
    },
    "question3": {
        "question": "What is the currency of Brazil?",
        "answer": "Real"
    },
    "question4": {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    "question5": {
        "question": "Which planet is known as the 'Red Planet'?",
        "answer": "Mars"
    },
    "question6": {
        "question": "What is the largest organ in the human body?",
        "answer": "Skin"
    },
    "question7": {
        "question": "Who is the author of the Harry Potter book series?",
        "answer": "J.K. Rowling"
    },
    "question8": {
        "question": "What is the chemical symbol for gold?",
        "answer": "Au"
    },
    "question9": {
        "question": "Which city hosted the 2016 Summer Olympics?",
        "answer": "Rio de Janeiro"
    },
    "question10": {
        "question": "Who is the current President of the United States?",
        "answer": "Joe Biden"
    },
}

score = 0 
for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print("Your score is: " + str(score))
    else:
        print("Wrong")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))


print("You got " + str(score) + " out of 10 questions correctly")
print("Your percentage is " + str(score//10 * 100) + " %")