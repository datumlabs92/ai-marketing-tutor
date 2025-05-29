
import json

with open("marketing_faq.json", "r") as f:
    faq = json.load(f)

with open("quiz.json", "r") as f:
    quiz = json.load(f)

def answer_question(question):
    for key in faq:
        if question.lower() in key.lower():
            return faq[key]
    return "Sorry, I don't know the answer to that. Try asking something else!"

def start_quiz():
    print("\nLet's take a quick quiz!")
    for q, options in quiz.items():
        print("\n" + q)
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        ans = input("Your answer (1-4): ")
        if options[int(ans)-1].lower() == options[0].lower():
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. Correct answer is: {options[0]}")

print("Hi, I'm your Marketing Tutor Bot! Ask me anything, or type 'quiz' to begin a quiz.")

while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]:
        break
    elif "quiz" in q.lower():
        start_quiz()
    else:
        print("Tutor:", answer_question(q))
