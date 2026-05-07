name = input("Enter your name: ")
mood = input("How are you feeling today? ").lower()

if "good" in mood or "great" in mood:
    print("Awesome,", name, "! Keep that energy going!")
elif "bad" in mood or "sad" in mood:
    print("Hey,", name, ", tough days happen. You got this.")
else:
    print("Interesting,", name, ". Thanks for sharing!")