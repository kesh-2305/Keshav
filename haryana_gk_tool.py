questions = [
    {
        "question": "What is the capital of Haryana?",
        "options": ["A. Delhi", "B. Chandigarh", "C. Jaipur", "D. Lucknow"],
        "answer": "B"
    },
    {
        "question": "Which language is mainly spoken in Haryana?",
        "options": ["A. Bengali", "B. Tamil", "C. Hindi", "D. Marathi"],
        "answer": "C"
    },
    {
        "question": "Which city in Haryana is famous for its IT and business hub?",
        "options": ["A. Gurugram", "B. Hisar", "C. Karnal", "D. Rohtak"],
        "answer": "A"
    },
    {
        "question": "Which national park is located in Haryana?",
        "options": ["A. Jim Corbett", "B. Ranthambore", "C. Sultanpur National Park", "D. Kaziranga"],
        "answer": "C"
    },
    {
        "question": "What is the state animal of Haryana?",
        "options": ["A. Tiger", "B. Nilgai", "C. Lion", "D. Elephant"],
        "answer": "B"
    },
    {
        "question": "What is the state bird of Haryana?",
        "options": ["A. Peacock", "B. Sparrow", "C. Eagle", "D. Duck"],
        "answer": "A"
    },
    {
        "question": "Which crop is Haryana especially known for?",
        "options": ["A. Wheat", "B. Basmati rice", "C. Cotton", "D. Tea"],
        "answer": "B"
    },
    {
        "question": "Which river is closely associated with Haryana?",
        "options": ["A. Ganga", "B. Brahmaputra", "C. Yamuna", "D. Godavari"],
        "answer": "C"
    },
]


def show_all_questions():
    print("\nHaryana GK Questions and Answers")
    print("-" * 35)
    for i, item in enumerate(questions, 1):
        print(f"{i}. {item['question']}")
        for option in item['options']:
            print(f"   {option}")
        print(f"   Correct Answer: {item['answer']}")


def quiz():
    score = 0
    print("\nHaryana GK Quiz")
    print("-" * 20)

    for i, item in enumerate(questions, 1):
        print(f"{i}. {item['question']}")
        for option in item['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == item['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}\n")

    print(f"Your score is {score} out of {len(questions)}")


def main():
    while True:
        print("\n1. Show all questions")
        print("2. Start quiz")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all_questions()
        elif choice == "2":
            quiz()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3")


if __name__ == "__main__":
    main()
