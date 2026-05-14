def get_user_input():
    name = input("Enter your name: ")
    mood = input("How are you feeling today? ").lower()
    return name, mood


def analyze_mood(name, mood):
    if "not good" in mood or "bad" in mood or "sad" in mood:
        return f"Sorry to hear that, {name}. Hope things improve!"
    elif "good" in mood or "great" in mood:
        return f"Awesome, {name}! Keep it up!"
    else:
        return f"Interesting, {name}. Thanks for sharing!"


def main():
    name, mood = get_user_input()
    response = analyze_mood(name, mood)
    print(response)


main()