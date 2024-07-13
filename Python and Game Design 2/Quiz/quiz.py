def load_questions(quiz_questions):
    questions = []
    with open(quiz_questions, 'r') as f:
        lines = f.readlines()
        question = ''
        options = []
        answer = ''
        for line in lines:
            line = line.strip()
            if line.startswith('Question'):
                if question:
                    questions.append((question, options, answer))
                question = line
                options = []
            elif line.startswith('Answer'):
                answer = line.split(': ')[1]
            else:
                options.append(line)
        questions.append((question, options, answer))
    return questions

def quiz(questions):
    score = 0
    for question, options, answer in questions:
        print(question)
        for option in options:
            print(options)
        user_answer = input("Your answer : ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions('quiz_questions.txt')
    quiz(questions)