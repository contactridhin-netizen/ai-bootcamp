import requests


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "name": data.get("login"),
            "repos": data.get("public_repos"),
            "followers": data.get("followers")
        }

    except Exception as e:
        print("Error occurred:", e)
        return None


def display_user_info(user_data):
    print("\n--- User Info ---")
    print(f"Username: {user_data['name']}")
    print(f"Public Repos: {user_data['repos']}")
    print(f"Followers: {user_data['followers']}")
    print("-" * 30)


def main():
    print("GitHub User Analyzer (type 'exit' to quit)\n")

    while True:
        username = input("Enter GitHub username: ")

        if username.lower() == "exit":
            print("Goodbye!")
            break

        user_data = fetch_github_user(username)

        if user_data is None:
            print("User not found or error occurred.\n")
        else:
            display_user_info(user_data)


main()