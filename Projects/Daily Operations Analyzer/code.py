def get_daily_data():
    print("\n--- Daily Operations Input ---")

    tasks = int(input("Tasks completed: "))
    hours = float(input("Hours worked: "))
    errors = int(input("Number of errors/issues: "))

    return tasks, hours, errors


def calculate_score(tasks, hours, errors):
    if hours == 0:
        return 0

    efficiency = tasks / hours
    penalty = errors * 2

    score = efficiency - penalty
    return round(score, 2)


def get_performance_label(score):
    if score >= 8:
        return "🔥 Excellent Performance"
    elif score >= 5:
        return "✅ Good Performance"
    elif score >= 2:
        return "⚠️ Average Performance"
    else:
        return "❌ Needs Improvement"


def main():
    print("OPS TRACKER PRO (type exit anytime later)\n")

    tasks, hours, errors = get_daily_data()

    score = calculate_score(tasks, hours, errors)
    label = get_performance_label(score)

    print("\n--- Daily Report ---")
    print(f"Tasks: {tasks}")
    print(f"Hours: {hours}")
    print(f"Errors: {errors}")
    print(f"Productivity Score: {score}")
    print(f"Status: {label}")


main()