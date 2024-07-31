import pyperclip

def ask_questions(questions):
    responses = []
    for question in questions:
        response = input(question + " ")
        responses.append(response)
    return responses

def print_responses(responses):
    for i, response in enumerate(responses, start=1):
        print(f"Answer {i}: {response}")

def main():
    # List of questions to ask
    questions = [
        "What is your name?",
        "How old are you?",
        "What is your favorite color?",
        "What city do you live in?"
    ]
    
    # Ask questions and collect responses
    responses = ask_questions(questions)
    
    # Print all responses
    print("\nHere are all your responses:")
    print_responses(responses)
    
    def copy_to_clipboard(text):
    pyperclip.copy(text)

if __name__ == "__main__":
    main()
