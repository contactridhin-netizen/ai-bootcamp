# GitHub Analyzer Pro

A Python CLI tool that fetches and analyzes GitHub user profiles using the GitHub REST API.

---

## Features

- Fetch GitHub user profile data
- Display key information (username, name, company, location, followers, repo count)
- Fetch public repositories using GitHub API
- Display top repositories sorted by star count ⭐
- Continuous CLI loop (analyze multiple users in one run)
- Exit anytime by typing `exit`
- Handles basic invalid input and API failures

---

## Technologies Used

- Python 3
- Requests library
- GitHub REST API

---

## How It Works

1. User enters a GitHub username
2. Program sends a request to GitHub user API
3. Program fetches repository data from a second API endpoint
4. Repositories are sorted by star count (highest first)
5. Top repositories are displayed in a formatted output

---

## Example Output

GitHub User Analysis

Username : torvalds
Name : Linus Torvalds
Company : Linux Foundation
Location : Portland, OR
Followers : 305610
Repos : 12

Top Repositories:
linux ⭐ 235243
uemacs ⭐ 2038
test-tlb ⭐ 1003

---

## Key Concepts Learned

- Working with REST APIs
- Handling JSON data in Python
- Using dictionaries and lists
- Sorting data using `lambda`
- Loop-based CLI applications
- Basic error handling and input validation

---

## Future Improvements

- Add repository language breakdown
- Show repo descriptions
- Add caching to reduce API calls
- Export results to CSV/JSON
- Add web version using Flask or Streamlit
- Add user “insight summary” (AI-style analysis)

---

## Author

Ridhin