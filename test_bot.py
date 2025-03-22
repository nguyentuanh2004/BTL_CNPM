import json
from difflib import get_close_matches
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
def find_best_match(user_question: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["intents"]:
        if q["patterns"] == question:
            return q["responses"]
def chat_bot():
    knowledge_base = load_knowledge_base("intents_output.json")
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            break
        best_match: str | None = find_best_match(user_input, [q["patterns"] for q in knowledge_base["intents"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print("Sorry, I didn't understand. Can you teach me?")
            new_answer: str = input('Type the answer or "skip" to skip: ')
            if new_answer.lower() != 'skip':
                knowledge_base["intents"].append({"patterns": user_input, "responses": new_answer})
                save_knowledge_base("intents_output.json", knowledge_base)
                print('Bot: Thank you! I learned that!')
def chat_bot_test():
    knowledge_base = load_knowledge_base("intents_output.json")
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            break
        best_match: str | None = find_best_match(user_input, [q["patterns"] for q in knowledge_base["intents"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print("Sorry, I didn't understand")
if __name__ == '__main__':
    chat_bot()