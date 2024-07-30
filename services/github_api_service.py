import requests
from abc import ABC, abstractmethod

class GitHubAPIService(ABC):
    @abstractmethod
    def get_user_data(self, endpoint):
        pass

    @abstractmethod
    def get_followers(self):
        pass

    @abstractmethod
    def get_following(self):
        pass

    @abstractmethod
    def unfollow_user(self, user_to_unfollow):
        pass

class GitHubAPIServiceImpl(GitHubAPIService):
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {self.token}"}

    def get_user_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_followers(self):
        return [user['login'] for user in self.get_user_data(f"users/{self.username}/followers")]

    def get_following(self):
        return [user['login'] for user in self.get_user_data(f"users/{self.username}/following")]

    def unfollow_user(self, user_to_unfollow):
        url = f"{self.base_url}/user/following/{user_to_unfollow}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 204
