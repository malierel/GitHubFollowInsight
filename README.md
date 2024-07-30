
---

# GitHubFollowInsight

**GitHubFollowInsight** is a Python-based desktop application that helps GitHub users identify followers and unfollowers. It provides a simple GUI interface built with Tkinter to manage your GitHub following list, making it easy to see who doesn't follow you back and allowing you to unfollow them if desired.

## Features

- **View Non-Followers**: Easily find out which users you are following who are not following you back.
- **Unfollow Users**: Unfollow users directly from the application.
- **Open Profiles**: Click on usernames to open their GitHub profiles in your web browser.
- **Secure**: Uses GitHub API tokens for secure access to your account data.

## Installation

### Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/malierel/GitHubFollowInsight.git
   cd GitHubFollowInsight
   ```

2. **Install dependencies:**

   It's recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

   Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your GitHub credentials:

   ```
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_github_token
   ```

   Replace `your_github_username` with your GitHub username and `your_github_token` with your personal access token. You can generate a personal access token on GitHub under **Settings > Developer settings > Personal access tokens**.

## Usage

Run the application using:

```bash
python main.py
```

This will open the Tkinter GUI. The application will automatically load your GitHub username and token from the `.env` file. Click the "Find" button to retrieve the list of users you are following who do not follow you back. You can choose to unfollow these users or open their GitHub profiles directly from the interface.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests should be made to the `main` branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact malierel@example.com.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI toolkit.
- [Requests](https://requests.readthedocs.io/en/latest/) - A simple, yet elegant HTTP library for Python.
- [Python-dotenv](https://github.com/theskumar/python-dotenv) - Manage environment variables in `.env` files.

---

Replace placeholders like `your_github_username` and `your_github_token` with actual values. Ensure that all links and contact details are accurate. This README provides a solid foundation and can be expanded with more details as needed.
