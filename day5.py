def get_user_input():
    name = input("Enter your name: ")
    if name.lower() == "exit":
        return None, None

    mood = input("How are you feeling today? ").lower()
    if mood == "exit":
        return None, None

    return name, mood


def analyze_mood(name, mood):
    if "not good" in mood or "bad" in mood or "sad" in mood:
        return f"Sorry to hear that, {name}. Hope things improve!"
    elif "good" in mood or "great" in mood:
        return f"Awesome, {name}! Keep it up!"
    else:
        return f"Interesting, {name}. Thanks for sharing!"


def main():
    print("Welcome to Mood Assistant (type 'exit' anytime to quit)\n")

    while True:
        name, mood = get_user_input()

        if name is None:
            print("Goodbye!")
            break

        response = analyze_mood(name, mood)
        print(response)
        print("-" * 40)


main()