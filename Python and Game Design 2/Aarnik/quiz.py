import random

def load_questions(quiz_file):
    """
    Load questions from a quiz file.

    Parameters:
    quiz_file (str): The path to the quiz file.

    Returns:
    list: A list of tuples, each containing a question, its options, and the correct answer.
    """
    questions = []
    with open(quiz_file, 'r') as f:
        lines = f.readlines()
        question = ''
        options = []
        answer = ''
        for line in lines:
            line = line.strip()
            if line.startswith('Question'):
                # If there's an existing question, add it to the list before starting a new one
                if question:
                    questions.append((question, options, answer))
                question = line
                options = []
            elif line.startswith('Answer'):
                answer = line.split(': ')[1]
            else:
                options.append(line)
        # Append the last question
        if question:
            questions.append((question, options, answer))
    return questions

def quiz(questions):
    """
    Run the quiz with the given questions.

    Parameters:
    questions (list): A list of tuples, each containing a question, its options, and the correct answer.
    """
    # Shuffle questions to ensure a different order each time the quiz is run
    random.shuffle(questions)
    score = 0
    learner_name = input("Enter your name: ").strip()
    print(f"\nWelcome, {learner_name}!")
    print(f"You will be answering {len(questions)} questions.\nGood luck!\n")

    for question, options, answer in questions:
        print(question)
        for option in options:
            print(option)
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answer}.")
        print()  # Print a blank line for better readability

    print(f"{learner_name}, your score: {score}/{len(questions)}")

if __name__ == "__main__":
    try:
        # Load questions from the file
        questions = load_questions('quiz.txt')
        # Start the quiz
        quiz(questions)
    except FileNotFoundError:
        print("The quiz file was not found. Please make sure 'quiz.txt' is in the correct directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
