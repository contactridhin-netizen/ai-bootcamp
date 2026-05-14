# GitHub User Analyzer

A simple Python CLI tool that fetches and displays GitHub user information using the GitHub API.

## Features

- Fetch user details (username, public repositories, followers)
- Handles invalid usernames gracefully
- Input validation
- Continuous user interaction (loop-based CLI)

## Technologies Used

- Python
- Requests library
- GitHub REST API

## How It Works

1. User enters a GitHub username
2. The program sends a request to GitHub API
3. Data is retrieved and displayed in a clean format
4. Handles errors like invalid users or network issues

## Example

Enter GitHub username: torvalds
========================================
GitHub User Info
========================================
Username       : torvalds
Public Repos   : 11
Followers      : 302834
========================================

## Future Improvements

- Add more user details (bio, location)
- Export data to file
- Build a simple web interface

## Author

Ridhin