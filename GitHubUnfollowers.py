import tkinter as tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Çevresel değişkenlerden bilgileri al
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# GitHub API fonksiyonları
def get_followers(username, token):
    url = f"https://api.github.com/users/{username}/followers"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return [user['login'] for user in response.json()]

def get_following(username, token):
    url = f"https://api.github.com/users/{username}/following"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return [user['login'] for user in response.json()]

def find_non_followers(username, token):
    followers = set(get_followers(username, token))
    following = set(get_following(username, token))
    non_followers = following - followers
    return list(non_followers)

# GUI fonksiyonları
def show_non_followers():
    username = GITHUB_USERNAME
    token = GITHUB_TOKEN
    non_followers = find_non_followers(username, token)
    non_followers_list.delete(0, tk.END)
    for user in non_followers:
        non_followers_list.insert(tk.END, user)

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("GitHub Non-Followers Finder")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Kullanıcı adı
ttk.Label(frame, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame, width=25)
username_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

# API Token
ttk.Label(frame, text="GitHub API Token:").grid(row=1, column=0, sticky=tk.W)
token_entry = ttk.Entry(frame, width=25, show="*")
token_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E))

# Bul butonu
ttk.Button(frame, text="Bul", command=show_non_followers).grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))

# Sonuç Listesi
non_followers_list = tk.Listbox(frame, height=10, width=50)
non_followers_list.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))

root.mainloop()
