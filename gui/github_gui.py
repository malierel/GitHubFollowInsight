import tkinter as tk
from tkinter import ttk
import webbrowser

class GitHubGUI:
    def __init__(self, root, non_followers_finder):
        self.root = root
        self.non_followers_finder = non_followers_finder
        self.setup_ui()

    def setup_ui(self):
        self.root.title("GitHub Non-Followers Finder")

        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(frame, width=25)
        self.username_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="GitHub API Token:").grid(row=1, column=0, sticky=tk.W)
        self.token_entry = ttk.Entry(frame, width=25, show="*")
        self.token_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Bul", command=self.show_non_followers).grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))

        self.results_frame = ttk.Frame(frame)
        self.results_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))
        self.results_frame.columnconfigure(0, weight=1)
        self.results_frame.columnconfigure(1, weight=0)

        self.unfollow_all_button = ttk.Button(frame, text="Unfollow All", command=self.unfollow_all_users)
        self.unfollow_all_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.unfollow_all_button.grid_remove()

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def show_non_followers(self):
        non_followers = self.non_followers_finder.find_non_followers()
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        for i, user in enumerate(non_followers):
            user_label = tk.Label(self.results_frame, text=user, fg="blue", cursor="hand2")
            user_label.grid(row=i, column=0, sticky=tk.W)
            user_label.bind("<Button-1>", lambda e, u=user: self.open_profile(u))

            unfollow_button = ttk.Button(self.results_frame, text="Unfollow", command=lambda u=user: self.unfollow_and_remove(u))
            unfollow_button.grid(row=i, column=1, sticky=tk.W)

        if non_followers:
            self.unfollow_all_button.grid(row=len(non_followers), column=0, columnspan=2, pady=10)
        else:
            self.unfollow_all_button.grid_remove()

    def unfollow_and_remove(self, user):
        if self.non_followers_finder.service.unfollow_user(user):
            self.show_non_followers()

    def unfollow_all_users(self):
        non_followers = self.non_followers_finder.find_non_followers()
        for user in non_followers:
            self.non_followers_finder.service.unfollow_user(user)
        self.show_non_followers()

    @staticmethod
    def open_profile(username):
        webbrowser.open(f"https://github.com/{username}")
