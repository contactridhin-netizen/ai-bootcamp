daily_records = []
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

def analyze_trends(records):
    if not records:
        print("No data available.\n")
        return

    scores = [r["score"] for r in records]

    avg_score = sum(scores) / len(scores)
    best_score = max(scores)
    worst_score = min(scores)

    print("\n--- Performance Insights ---")
    print(f"Average Score: {round(avg_score, 2)}")
    print(f"Best Score   : {best_score}")
    print(f"Worst Score  : {worst_score}")
    
def main():
    print("OPS TRACKER PRO (type exit anytime)\n")

    while True:
        choice = input("\nAdd new entry? (yes/view/analyze/exit): ").lower()

        if choice == "exit":
            print("Goodbye!")
            break

        if choice == "view":
            print("\n--- ALL RECORDS ---")
            for i, record in enumerate(daily_records, 1):
                print(f"Day {i}: {record}")
            continue
        
        if choice == "analyze":
            analyze_trends(daily_records)
            continue

        if choice != "yes":
            print("Invalid option")
            continue

        tasks, hours, errors = get_daily_data()

        score = calculate_score(tasks, hours, errors)
        label = get_performance_label(score)

        record = {
            "tasks": tasks,
            "hours": hours,
            "errors": errors,
            "score": score,
            "status": label
        }

        daily_records.append(record)

        print("\n--- Daily Report ---")
        print(f"Score: {score}")
        print(f"Status: {label}")


main()