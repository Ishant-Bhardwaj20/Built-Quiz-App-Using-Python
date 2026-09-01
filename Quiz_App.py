def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Haryana", "B) Oddisha", "C) New Delhi", "D) Pune"],
            "answer": "C) New Delhi"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B) 4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C) William Shakespeare"
        }, 
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A) H2O"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "answer": "B) Blue Whale"
        }
    ]

    score = 0
 
    for index,q in enumerate(questions):  
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer(A/B/C/D): ") 
        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")

run_quiz()
