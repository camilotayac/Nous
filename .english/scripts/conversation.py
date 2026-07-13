#!/usr/bin/env python3
"""
Conversation mode: practice English speaking with rule-based or LLM fallback.
"""
import os
import sys
import random

sys.path.insert(0, os.path.dirname(__file__))

CONVERSATION_STARTERS = [
    "Hi! How are you doing today?",
    "What did you do today?",
    "Tell me about your favorite subject.",
    "What are you learning in school?",
    "Do you like science? Why or why not?",
    "What's the weather like today?",
    "What are your plans for this weekend?",
    "Can you describe your favorite food?",
    "What's the most interesting thing you've learned recently?",
    "Do you prefer reading or watching videos? Why?",
]

VOCAB_THEMES = {
    "science": ["reaction", "energy", "velocity", "catalyst", "concentration", "temperature"],
    "math": ["equation", "function", "variable", "theorem", "probability", "matrix"],
    "daily": ["hello", "please", "thank you", "good morning", "how are you", "goodbye"],
    "feelings": ["happy", "sad", "excited", "tired", "interested", "confused"],
}

FOLLOW_UPS = {
    "question": [
        "Can you tell me more about that?",
        "Why do you think so?",
        "How does that make you feel?",
        "That's interesting! What else?",
        "Can you give me an example?",
    ],
    "agreement": [
        "I agree! That's a good point.",
        "Exactly! Anything else?",
        "Right! What else do you think?",
    ],
    "encouragement": [
        "Great job! Keep going!",
        "You're doing well! Try to say more.",
        "Nice! Can you use that word in a sentence?",
    ],
}


def check_api_key():
    return os.environ.get("OPENAI_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")


def try_llm_response(user_text, history):
    api_key = check_api_key()
    if not api_key:
        return None

    try:
        if os.environ.get("OPENAI_API_KEY"):
            import openai
            client = openai.OpenAI()
            messages = [
                {"role": "system", "content": (
                    "You are a friendly English tutor for a Spanish-speaking student. "
                    "Keep responses short (1-2 sentences). Correct grammar gently. "
                    "Use simple vocabulary. Encourage the student to practice more."
                )}
            ]
            for h in history[-6:]:
                messages.append({"role": h["role"], "content": h["content"]})
            messages.append({"role": "user", "content": user_text})
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=100,
            )
            return response.choices[0].message.content

        elif os.environ.get("ANTHROPIC_API_KEY"):
            import anthropic
            client = anthropic.Anthropic()
            system = (
                "You are a friendly English tutor for a Spanish-speaking student. "
                "Keep responses short (1-2 sentences). Correct grammar gently. "
                "Use simple vocabulary. Encourage the student to practice more."
            )
            conversation = []
            for h in history[-6:]:
                conversation.append({"role": h["role"], "content": h["content"]})
            conversation.append({"role": "user", "content": user_text})
            response = client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=100,
                system=system,
                messages=conversation,
            )
            return response.content[0].text
    except Exception:
        pass
    return None


def rule_response(user_text, history):
    user_lower = user_text.lower().strip()

    if any(w in user_lower for w in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How are you today?",
            "Hi there! What would you like to talk about?",
            "Hey! Nice to see you. How's it going?",
        ])

    if any(w in user_lower for w in ["how are you", "how do you do"]):
        return random.choice([
            "I'm doing great, thanks! And you?",
            "I'm fine! What about you?",
            "Good! Ready to practice English?",
        ])

    if any(w in user_lower for w in ["thank", "thanks"]):
        return random.choice([
            "You're welcome! Keep practicing!",
            "No problem! You're doing great!",
            "My pleasure! Try using a new word next time.",
        ])

    if any(w in user_lower for w in ["bye", "goodbye", "see you"]):
        return random.choice([
            "Goodbye! Keep practicing every day!",
            "See you! You're making great progress!",
            "Bye! Don't forget to review your vocabulary!",
        ])

    if "?" in user_text:
        return random.choice(FOLLOW_UPS["question"])

    words = user_text.split()
    if len(words) < 3:
        return random.choice(FOLLOW_UPS["encouragement"])

    if any(w in user_lower for w in ["yes", "no", "maybe", "i think"]):
        return random.choice(FOLLOW_UPS["agreement"])

    vocab_words = []
    for theme_words in VOCAB_THEMES.values():
        for w in theme_words:
            if w in user_lower:
                vocab_words.append(w)

    if vocab_words:
        word = random.choice(vocab_words)
        return f"Great use of '{word}'! Can you tell me more about that?"

    return random.choice(FOLLOW_UPS["question"])


def conversation_session():
    print("\n💬 Modo Conversación — Practica inglés")
    print("   Escribe en inglés y yo te respondo.")
    print("   Comandos: 'q' salir, 'h' hablar con audio\n")

    history = []
    use_audio = True
    starter = random.choice(CONVERSATION_STARTERS)
    print(f"🤖 Yo: {starter}")
    history.append({"role": "assistant", "content": starter})

    if use_audio:
        try:
            from utils.audio import speak
            speak(starter)
        except Exception:
            pass

    while True:
        try:
            user_input = input("\n>Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 ¡Hasta luego!")
            return

        if not user_input:
            continue
        if user_input.lower() == "q":
            print("👋 ¡Hasta luego!")
            return
        if user_input.lower() == "h":
            use_audio = not use_audio
            print(f"   Audio: {'ON' if use_audio else 'OFF'}")
            continue

        history.append({"role": "user", "content": user_input})

        response = try_llm_response(user_text=user_input, history=history)

        if response is None:
            response = rule_response(user_text=user_input, history=history)

        print(f"\n🤖 Yo: {response}")
        history.append({"role": "assistant", "content": response})

        if use_audio:
            try:
                from utils.audio import speak
                speak(response)
            except Exception:
                pass


if __name__ == "__main__":
    conversation_session()
