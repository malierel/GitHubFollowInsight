Here's a draft for a `README.md` file for the `GitHubFollowInsight` project:

---

# GitHubFollowInsight

GitHubFollowInsight is a Python application designed to help users manage their GitHub followings. It identifies GitHub users that you follow but do not follow you back, and offers features to manage these connections easily through a graphical user interface (GUI).

## Features

- **List Non-Followers**: Displays a list of GitHub users you follow who do not follow you back.
- **Unfollow Individual Users**: Allows you to unfollow users directly from the app.
- **Unfollow All**: Provides an option to unfollow all non-followers in one action.
- **Profile Links**: Access user profiles directly by clicking on usernames.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/malierel/GitHubFollowInsight.git
   cd GitHubFollowInsight
   ```

2. **Install dependencies**:
   ```bash
   pip install requests python-dotenv
   ```

3. **Setup environment variables**:
   Create a `.env` file in the root directory with your GitHub username and personal access token:
   ```
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_personal_access_token
   ```

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Using the GUI**:
   - Enter your GitHub username and token if not set in `.env`.
   - Click "Find" to list users you follow who don't follow you back.
   - Click "Unfollow" to unfollow specific users or "Unfollow All" to unfollow all non-followers.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request. Ensure your code follows best practices and includes documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project utilizes the GitHub API to interact with GitHub data.

---

Feel free to modify or expand upon this template to better suit the specific details and style you want for your project.
