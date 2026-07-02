import random
import re
from datetime import datetime


def get_response(user_input):
    text = user_input.lower().strip()

    greetings = [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊",
        "Hey! Nice to meet you.",
        "Hello! What can I do for you?"
    ]

    greeting_patterns = [
        r"\bhi\b",
        r"\bhello\b",
        r"\bhey\b"
    ]

    for pattern in greeting_patterns:
        if re.search(pattern, text):
            return random.choice(greetings)

    if re.search(r"how are you", text):
        return random.choice([
            "I'm doing great! Thanks for asking. 😊",
            "I'm fine and ready to help!",
            "Doing awesome! What about you?"
        ])

    elif re.search(r"(your name|who are you)", text):
        return "I'm CodBot 🤖, a rule-based AI chatbot."

    elif re.search(r"(created you|made you|developer)", text):
        return "I was created by Agalya as part of the CodSoft AI Internship."

    elif re.search(r"(time|current time)", text):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif re.search(r"(date|today)", text):
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif re.search(r"(thank you|thanks)", text):
        return random.choice([
            "You're welcome! 😊",
            "Glad I could help!",
            "Anytime!"
        ])

    elif re.search(r"(bye|goodbye|see you)", text):
        return random.choice([
            "Goodbye! Have a wonderful day! 👋",
            "See you soon!",
            "Take care!"
        ])

    elif re.search(r"(help)", text):
        return (
            "You can ask me about:\n"
            "• My name\n"
            "• Current time\n"
            "• Today's date\n"
            "• Who created me\n"
            "• Greetings\n"
            "• Say bye"
        )

    else:
        unknown_responses = [
            "Sorry, I didn't understand that.",
            "Could you please rephrase your question?",
            "I'm still learning. Try asking something else.",
            "I don't have an answer for that yet."
        ]

        return random.choice(unknown_responses)