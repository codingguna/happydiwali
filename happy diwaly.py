import time
import random

def display_fireworks():
    fireworks = [
        "🎆✨🎇",
        "🎇✨🎆",
        "✨🎇🎆",
        "🎆🎇✨"
    ]
    for _ in range(5):  # Display fireworks 5 times
        print(random.choice(fireworks))
        time.sleep(1)

def diwali_message():
    print("🌟🌟 Happy Diwali! 🌟🌟")
    time.sleep(1)
    print("May your life be filled with light and joy!")
    time.sleep(1)
    print("Let's celebrate with fireworks and sweets! 🍬")
    time.sleep(1)


diwali_message()
display_fireworks()
print("Wishing you a prosperous and joyful Diwali! 🎉")
print("Thank you for celebrating with us!")

