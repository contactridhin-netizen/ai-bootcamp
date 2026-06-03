# GitHub User Analyzer
# Fetches and displays GitHub user data using API

import requests


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.json()

    except:
        return None


def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return []

        repos = response.json()

        # sort by stars (simple sorting)
        repos.sort(key=lambda x: x["stargazers_count"], reverse=True)

        return repos[:5]  # top 5 repos

    except:
        return []


def display_user(data, repos):
    print("\n" + "=" * 50)
    print(" GITHUB USER ANALYSIS ")
    print("=" * 50)

    print(f"Username   : {data.get('login')}")
    print(f"Name       : {data.get('name')}")
    print(f"Company    : {data.get('company')}")
    print(f"Location   : {data.get('location')}")
    print(f"Followers  : {data.get('followers')}")
    print(f"Repos      : {data.get('public_repos')}")

    print("\nTop Repositories:")
    print("-" * 50)

    if not repos:
        print("No repositories found")
    else:
        for repo in repos:
            print(f"{repo['name']} ⭐ {repo['stargazers_count']}")

    print("=" * 50 + "\n")


def main():
    print("GitHub Analyzer Pro (type 'exit' to quit)\n")

    while True:
        username = input("Enter GitHub username: ").strip()

        if username.lower() == "exit":
            print("Goodbye!")
            break

        if username == "":
            print("Please enter a valid username\n")
            continue

        user_data = fetch_github_user(username)

        if user_data is None:
            print("User not found or API error\n")
            continue

        repos = fetch_repos(username)

        display_user(user_data, repos)


main()