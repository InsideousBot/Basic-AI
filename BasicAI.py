import random

# Define a simple knowledge base
knowledge_base = {
    "greetings": ["hello", "hi", "hey"],
    "goodbyes": ["goodbye", "bye", "see you later"],
    "thanks": ["thanks", "thank you", "appreciate it"],
    "responses": {
        "greetings": ["Hi there!", "Hello!", "Hey!"],
        "goodbyes": ["Goodbye!", "Bye! See you later!", "Take care!"],
        "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
        "unknown": ["I'm not sure how to respond.", "Could you rephrase that?", "I don't understand."]
    }
}

def respond(user_input):
    user_input = user_input.lower()
    
    if any(word in user_input for word in knowledge_base["greetings"]):
        return random.choice(knowledge_base["responses"]["greetings"])
    elif any(word in user_input for word in knowledge_base["goodbyes"]):
        return random.choice(knowledge_base["responses"]["goodbyes"])
    elif any(word in user_input for word in knowledge_base["thanks"]):
        return random.choice(knowledge_base["responses"]["thanks"])
    else:
        return random.choice(knowledge_base["responses"]["unknown"])

print("Basic AI Chatbot. Type 'quit' to exit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break

    response = respond(user_input)
    print("AI: ", response)
