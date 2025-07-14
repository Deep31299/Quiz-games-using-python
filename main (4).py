import time
import json

# Question bank
quiz_data = {
    "General Knowledge": [
        {"question": "Capital of India?", "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "answer": "B"},
        {"question": "Largest continent?", "options": ["A. Asia", "B. Europe", "C. Africa", "D. Australia"], "answer": "A"},
        {"question": "National animal of India?", "options": ["A. Tiger", "B. Lion", "C. Elephant", "D. Leopard"], "answer": "A"},
        {"question": "Currency of USA?", "options": ["A. Dollar", "B. Peso", "C. Rupee", "D. Yen"], "answer": "A"},
        {"question": "Longest river?", "options": ["A. Ganga", "B. Amazon", "C. Nile", "D. Yangtze"], "answer": "C"}
    ],
    "Science": [
        {"question": "Plants absorb which gas?", "options": ["A. Oxygen", "B. Nitrogen", "C. CO2", "D. Hydrogen"], "answer": "C"},
        {"question": "Boiling point of water?", "options": ["A. 90°C", "B. 100°C", "C. 120°C", "D. 80°C"], "answer": "B"},
        {"question": "Which organ pumps blood?", "options": ["A. Brain", "B. Liver", "C. Kidney", "D. Heart"], "answer": "D"},
        {"question": "Sun is a?", "options": ["A. Planet", "B. Star", "C. Comet", "D. Asteroid"], "answer": "B"},
        {"question": "Gas essential for breathing?", "options": ["A. Nitrogen", "B. Oxygen", "C. CO2", "D. Helium"], "answer": "B"}
    ],
    "Mental Maths": [
        {"question": "15 + 28 = ?", "options": ["A. 43", "B. 40", "C. 33", "D. 35"], "answer": "A"},
        {"question": "12 × 3 - 6 ÷ 2 = ?", "options": ["A. 33", "B. 36", "C. 30", "D. 18"], "answer": "A"},
        {"question": "Square of 6?", "options": ["A. 12", "B. 36", "C. 18", "D. 24"], "answer": "B"},
        {"question": "50% of 80?", "options": ["A. 50", "B. 30", "C. 40", "D. 60"], "answer": "C"},
        {"question": "25 ÷ 5 = ?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "C"}
    ],
    "English Language": [
        {"question": "Synonym of 'Happy'?", "options": ["A. Sad", "B. Angry", "C. Joyful", "D. Serious"], "answer": "C"},
        {"question": "He ___ going to school.", "options": ["A. is", "B. are", "C. were", "D. am"], "answer": "A"},
        {"question": "Opposite of 'Big'?", "options": ["A. Large", "B. Huge", "C. Small", "D. Tall"], "answer": "C"},
        {"question": "Plural of 'Child'?", "options": ["A. Childs", "B. Childes", "C. Children", "D. Childer"], "answer": "C"},
        {"question": "I ___ a book yesterday.", "options": ["A. read", "B. reads", "C. reading", "D. will read"], "answer": "A"}
    ]
}

QUESTION_TIME_LIMIT = 15
SCORE_FILE = "quiz_scores.json"

# Load high score
try:
    with open(SCORE_FILE, "r") as file:
        score_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    score_data = {"high_score": 0}

print("🎮 Welcome to the Ultimate Quiz Game!\n")
print("📚 Categories:")
categories = list(quiz_data.keys())

for i, cat in enumerate(categories, start=1):
    print(f"{i}. {cat}")

# Choose category
while True:
    try:
        cat_choice = int(input("\nEnter category number: "))
        if 1 <= cat_choice <= len(categories):
            selected_category = categories[cat_choice - 1]
            break
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a number.")

questions = quiz_data[selected_category]
score = 0
results = []

print(f"\n📝 Starting quiz on '{selected_category}'. You have {QUESTION_TIME_LIMIT} sec/question.\n")

# Ask questions
for index, q in enumerate(questions, start=1):
    print(f"Q{index}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    start = time.time()
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    elapsed = time.time() - start

    if elapsed > QUESTION_TIME_LIMIT:
        print("⏰ Time's up!\n")
        correct = "No"
        selected = "No Answer"
    elif answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
        correct = "Yes"
        selected = answer
    else:
        print(f"❌ Wrong! Correct: {q['answer']}\n")
        correct = "No"
        selected = answer

    results.append([f"Q{index}", selected, q['answer'], correct])

# Display result in manual table format
print("📊 Final Result Summary:\n")
print(f"{'Q#':<5} {'Your Answer':<15} {'Correct Answer':<17} {'Correct?':<10}")
print("-" * 50)
for row in results:
    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<17} {row[3]:<10}")

# Final score and high score
print(f"\n🎯 Your Score: {score}/{len(questions)}")

if score > score_data.get("high_score", 0):
    print("🏆 New High Score!")
    score_data["high_score"] = score
    with open(SCORE_FILE, "w") as file:
        json.dump(score_data, file)
else:
    print(f"🥇 High Score to Beat: {score_data.get('high_score', 0)}")

print("🎉 Thanks for playing!")

