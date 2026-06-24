print("=" * 60)
print("🤖 Welcome to RuleBot AI Assistant")
print("=" * 60)

name = input("Before we begin, what's your name? ")

print(f"\nHello {name}! 👋")
print("I'm RuleBot, your personal AI Assistant.")

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 AVAILABLE COMMANDS

👋 Greetings
• hello
• hi

💬 General Questions
• how are you
• what is your name
• who created you
• thank you
• thanks
• bye

🧠 AI Knowledge
• what is ai
• what is machine learning
• what is deep learning
• what is chatbot

🎉 Fun Features
• tell me a joke
• fun fact

📝 Other Commands
• menu  (show this menu again)
• exit  (close the chatbot)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print(f"What would you like me to do today, {name}?")
print("Type a command or type 'menu' anytime to see all options.\n")

responses = {
    "hello": f"Hello {name}! 👋",
    "hi": f"Hi {name}! 👋",
    "how are you": "I'm doing great! Thanks for asking. 😊",
    "what is your name": "My name is RuleBot AI Assistant.",
    "who created you": "I was created by Kshama Jain as part of the DecodeLabs AI Internship.",
    "thank you": "You're welcome! 😊",
    "thanks": "Happy to help! 😊",
    "bye": f"Goodbye {name}! Have a wonderful day! 👋"
}

ai_info = {
    "what is ai":
    "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",

    "what is machine learning":
    "Machine Learning is a branch of AI that allows computers to learn from data and improve automatically.",

    "what is deep learning":
    "Deep Learning is a subset of Machine Learning that uses neural networks with many layers.",

    "what is chatbot":
    "A chatbot is a computer program designed to simulate conversations with users."
}

while True:

    user_input = input(f"\n{name}: ")
    clean_input = user_input.lower().strip()

    # Exit
    if clean_input == "exit":
        print(f"\n🤖 RuleBot: Goodbye {name}! Thanks for chatting with me.")
        break

    # Menu
    elif clean_input == "menu":
        print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 AVAILABLE COMMANDS

👋 Greetings
• hello
• hi

💬 General Questions
• how are you
• what is your name
• who created you
• thank you
• thanks
• bye

🧠 AI Knowledge
• what is ai
• what is machine learning
• what is deep learning
• what is chatbot

🎉 Fun Features
• tell me a joke
• fun fact

📝 Other Commands
• menu
• exit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    # AI Questions
    elif clean_input in ai_info:
        print("\n🤖 RuleBot:", ai_info[clean_input])

    # Joke
    elif clean_input == "tell me a joke":
        print("\n🤖 RuleBot: Why did the computer go to the doctor?")
        print("🤖 RuleBot: Because it caught a virus! 😂")

    # Fun Fact
    elif clean_input == "fun fact":
        print("\n🤖 RuleBot: The first AI program was developed in the 1950s! 🤯")

    # General Responses
    elif clean_input in responses:
        print("\n🤖 RuleBot:", responses[clean_input])

    # Unknown Command
    else:
        print("\n🤖 RuleBot: Sorry, I don't understand that.")
        print("🤖 RuleBot: Type 'menu' to see everything I can do.")