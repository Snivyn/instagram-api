import json
from src.api import API as InstagramAPI

if __name__ == "__main__":
    api = InstagramAPI(username="sza")
    metadata = api.fetch_user_metadata()
    posts = api.fetch_posts()
    reels = api.fetch_reels()
    print(json.dumps({"metadata": metadata, "posts": posts, "reels": reels}, indent=4))
