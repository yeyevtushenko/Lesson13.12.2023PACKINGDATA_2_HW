import json
import os

def survey():
    survey = {
        "question": "Яка на Вашу думку найпростіша мова програмування?",
        "options": ["Python", "Java", "JavaScript", "C++", "Інша"]
    }

    responses = []

    print("Питання: {}".format(survey["question"]))
    print("Відповіді: {}".format(", ".join(survey["options"])))

    while True:
        response = input("Ваша відповідь (введіть 'exit' щоб завершити): ")

        if response.lower() == 'exit':
            break

        if response in survey["options"]:
            responses.append(response)
            print("Відповідь записана.")
        else:
            print("Невірна відповідь. Виберіть із запропонованих варіантів.")

    return responses

def save(responses):
    filename = "Результати опитування.json"

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            data.append(responses)
    else:
        data = [responses]

    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    print("Ласкаво просимо до програми опитування!")

    while True:
        user_input = input("Бажаєте взяти участь в опитуванні? (так/ні): ")

        if user_input.lower() == 'так':
            user_responses = survey()
            save(user_responses)
            print("Дякуємо за участь в опитуванні! Вашу відповідь записано.")
        elif user_input.lower() == 'ні':
            print("Допобачення!")
            break
        else:
            print("Некоректний ввід. Будь ласка, введіть 'так' або 'ні'.")

if __name__ == "__main__":
    main()