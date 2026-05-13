import requests


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code == 404:
            return "not_found"

        if response.status_code != 200:
            return "error"

        data = response.json()

        return {
            "name": data.get("login"),
            "repos": data.get("public_repos"),
            "followers": data.get("followers")
        }

    except Exception:
        return "error"


def display_user_info(user_data):
    print("\n" + "=" * 40)
    print("GitHub User Info")
    print("=" * 40)
    print(f"Username       : {user_data['name']}")
    print(f"Public Repos   : {user_data['repos']}")
    print(f"Followers      : {user_data['followers']}")
    print("=" * 40 + "\n")


def get_username():
    username = input("Enter GitHub username: ").strip()

    if username == "":
        print("Username cannot be empty.\n")
        return None

    return username


def main():
    print("GitHub Analyzer (type 'exit' to quit)\n")

    while True:
        username = get_username()

        if username is None:
            continue

        if username.lower() == "exit":
            print("Goodbye!")
            break

        result = fetch_github_user(username)

        if result == "not_found":
            print("User not found. Try again.\n")
        elif result == "error":
            print("Something went wrong. Please try later.\n")
        else:
            display_user_info(result)


main()