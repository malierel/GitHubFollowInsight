from services.github_service_factory import GitHubServiceFactory
from services.non_followers_finder import NonFollowersFinder
from gui.github_gui import GitHubGUI
import tkinter as tk
from utils.dotenv_loader import load_env_vars

if __name__ == "__main__":
    GITHUB_USERNAME, GITHUB_TOKEN = load_env_vars()

    service = GitHubServiceFactory.create_service(GITHUB_USERNAME, GITHUB_TOKEN)
    non_followers_finder = NonFollowersFinder(service)

    root = tk.Tk()
    gui = GitHubGUI(root, non_followers_finder)
    root.mainloop()
