# Rule-Based Chatbot
while True:
    user = input("You: ").lower()
    if user in ["hi","hello"]:
        print("Bot: Hello!")
    elif user == "how are you":
        print("Bot: I am fine.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
