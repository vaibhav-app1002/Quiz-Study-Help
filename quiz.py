def load_questions(filename):
    questions = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    for i in range(0, len(lines), 4):
        q = lines[i]
        options = lines[i+1:i+4]
        answer = lines[i+4] if i+4 < len(lines) else None
        questions.append((q, options[:-1], options[-1]))
    return questions


def load_questions_fixed(filename):
    questions = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    for i in range(0, len(lines), 4):
        q = lines[i]
        choices = lines[i+1:i+3]
        choices.append(lines[i+3])
        ans = lines[i+4] if i+4 < len(lines) else None
        questions.append((q, choices, ans))
    return questions


def load_questions(filename):
    questions = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    for i in range(0, len(lines), 5):
        q = lines[i]
        choices = lines[i+1:i+4]
        ans = lines[i+4].upper()
        questions.append((q, choices, ans))
    return questions


def quiz_game():
    questions = load_questions("questions.txt")
    score = 0

    print("🧠 Welcome to the Quiz Game!\n")

    for i, (q, choices, ans) in enumerate(questions, 1):
        print(f"Q{i}: {q}")
        for choice in choices:
            print(choice)
        user = input("Your answer (A/B/C): ").upper()

        if user == ans:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {ans}\n")

    print(f"Final Score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()
