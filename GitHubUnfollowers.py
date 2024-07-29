import tkinter as tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os
import webbrowser

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

def unfollow_user(username, token, user_to_unfollow):
    url = f"https://api.github.com/user/following/{user_to_unfollow}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully unfollowed {user_to_unfollow}")
    else:
        print(f"Failed to unfollow {user_to_unfollow}")
    return response.status_code == 204

def unfollow_all_users(username, token, users):
    for user in users:
        unfollow_user(username, token, user)

# Kullanıcı profilini açma
def open_profile(username):
    webbrowser.open(f"https://github.com/{username}")

# GUI fonksiyonları
def show_non_followers():
    non_followers = find_non_followers(GITHUB_USERNAME, GITHUB_TOKEN)
    for widget in results_frame.winfo_children():
        widget.destroy()  # Önceki sonuçları temizle
    for i, user in enumerate(non_followers):
        # Kullanıcı adı label'ı
        user_label = tk.Label(results_frame, text=user, fg="blue", cursor="hand2")
        user_label.grid(row=i, column=0, sticky=tk.W)
        user_label.bind("<Button-1>", lambda e, u=user: open_profile(u))  # Tıklama olayını bağla
        # Unfollow butonu
        unfollow_button = ttk.Button(results_frame, text="Unfollow",
                                     command=lambda u=user: unfollow_and_remove(u))
        unfollow_button.grid(row=i, column=1)

    # "Unfollow All" butonunu güncelle
    if non_followers:
        unfollow_all_button.grid(row=len(non_followers), column=0, columnspan=2, pady=10)
    else:
        unfollow_all_button.grid_remove()

def unfollow_and_remove(user):
    if unfollow_user(GITHUB_USERNAME, GITHUB_TOKEN, user):
        show_non_followers()  # Listeden kullanıcıyı çıkar ve güncelle

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("GitHub Non-Followers Finder")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Kullanıcı adı ve API Token (şimdilik GUI'den kaldırıldı)
ttk.Label(frame, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame, width=25)
username_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))
username_entry.insert(0, GITHUB_USERNAME)  # Varsayılan olarak .env dosyasından

ttk.Label(frame, text="GitHub API Token:").grid(row=1, column=0, sticky=tk.W)
token_entry = ttk.Entry(frame, width=25, show="*")
token_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E))
token_entry.insert(0, GITHUB_TOKEN)  # Varsayılan olarak .env dosyasından

# Bul butonu
ttk.Button(frame, text="Bul", command=show_non_followers).grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))

# Sonuç Listesi
results_frame = ttk.Frame(frame)
results_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))

# "Unfollow All" butonu
unfollow_all_button = ttk.Button(frame, text="Unfollow All", command=lambda: unfollow_all_users(GITHUB_USERNAME, GITHUB_TOKEN, find_non_followers(GITHUB_USERNAME, GITHUB_TOKEN)))
unfollow_all_button.grid(row=4, column=0, columnspan=3, pady=10)
unfollow_all_button.grid_remove()  # Başlangıçta gizle

root.mainloop()
