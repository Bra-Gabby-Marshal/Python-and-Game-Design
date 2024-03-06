# Define a dictionary to store the quiz questions, each with a list of possible answers and the correct answer
quiz_questions = {
    "What is the capital of France?": {
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    },
    "What is the chemical symbol for water?": {
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    },
    "What is the largest planet in our solar system?": {
        "options": ["A. Mercury", "B. Venus", "C. Earth", "D. Jupiter"],
        "answer": "D"
    },
    "What year did the Titanic sink?": {
        "options": ["A. 1910", "B. 1912", "C. 1920", "D. 1930"],
        "answer": "B"
    }
}

# Function to administer the quiz
def administer_quiz(questions):
    score = 0
    total_questions = len(questions)

    # Iterate over each question in the quiz
    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        user_answer = input("Your answer (Enter the letter corresponding to your choice): ")

        # Check if the user's answer is correct
        if user_answer.upper() == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {data['answer']}")

    # Display the final score
    print(f"\nQuiz completed! You scored {score} out of {total_questions}.")

# Main function to start the quiz
def main():
    print("Welcome to the Quiz!")

    # Administer the quiz
    administer_quiz(quiz_questions)

# Execute the main function
if __name__ == "__main__":
    main()
