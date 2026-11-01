def display_welcome():
    print("\n====================================")
    print("       WELCOME TO PYTHON CHATBOT")
    print("====================================")
    print("Chatbot: Hello! I am your chatbot.")
    print("Chatbot: Type 'help' for commands.")
    print("Chatbot: Type 'bye' to exit.")
    print("------------------------------------")


def get_response(user_message):
    message = user_message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you."

    elif message == "how are you":
        return "I'm fine, thanks! How can I help you?"

    elif message == "what is your name":
        return "I am a Python-based chatbot."

    elif message == "what can you do":
        return "I can respond to simple predefined messages."

    elif message == "help":
        return "Available commands: hello, how are you, what is your name, what can you do, bye"

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day."

    elif message == "":
        return "Please enter a message."

    else:
        return "Sorry, I don't understand that message."


def start_chatbot():
    display_welcome()

    while True:
        user_message = input("\nYou: ")
        response = get_response(user_message)

        print("Chatbot:", response)

        if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    start_chatbot()