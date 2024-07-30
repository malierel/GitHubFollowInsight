from dotenv import load_dotenv
import os

def load_env_vars():
    load_dotenv()
    username = os.getenv("GITHUB_USERNAME", "").strip()
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if not username or not token:
        raise ValueError("GitHub credentials not set in .env file.")
    return username, token
