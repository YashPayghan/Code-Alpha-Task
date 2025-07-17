import random
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open!",
    "What do you call a computer that sings? A-Dell.",
    "Why don’t robots ever panic? They have nerves of steel.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why can’t your nose be 12 inches long? Because then it would be a foot.",
    "Did you hear about the claustrophobic astronaut? He just needed a little space.",
    "Why was 6 afraid of 7? Because 7 8 (ate) 9.",
    "Why did the math book look sad? Because it had too many problems.",
    "How do you make 7 even? Take away the 's'.",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why can’t Elsa from Frozen have a balloon? Because she will let it go.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

print(" ChatBot: Hello! I'm your chatbot. Type 'joke' for a joke or 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello there! How can I help you?")
    elif "name" in user_input:
        print("ChatBot: I'm ChatBot, your virtual buddy.")
    elif "how are you" in user_input:
        print("ChatBot: I'm just a bunch of code, but I'm doing great! ")
    elif "joke" in user_input:
        print("ChatBot:", random.choice(jokes))
    elif user_input == "bye":
        print("ChatBot: Goodbye! Have a nice day! ")
        break
    else:
        print("ChatBot: Hmm... I don't understand that. Try asking something else.")