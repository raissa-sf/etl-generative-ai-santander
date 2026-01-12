import os
from config.config import PROCESSED_DIR
from .utils import load_json, save_json


def load_users(users: list, output_dir: str = PROCESSED_DIR):
    """
    Saves each user with personalized news to a JSON file,
    appending new messages without overwriting existing ones
    and ensuring the JSON field order matches the Santander API.
    """
    os.makedirs(output_dir, exist_ok=True)

    for user in users:
        user_id = user.get("id")
        output_path = os.path.join(output_dir, f"user_{user_id}.json")

        existing_user_data = load_json(output_path) or {"news": []}

        # Merge news without duplicates
        existing_news_ids = {
            news_item["id"]
            for news_item in existing_user_data.get("news", [])
        }

        for new_message in user.get("news", []):
            if new_message["id"] not in existing_news_ids:
                existing_user_data.setdefault("news", []).append(new_message)

        # Update other fields
        for field, value in user.items():
            if field != "news":
                existing_user_data[field] = value

        # Explicit order
        ordered_user_data = {
            "id": existing_user_data.get("id"),
            "name": existing_user_data.get("name"),
            "account": existing_user_data.get("account"),
            "card": existing_user_data.get("card"),
            "features": existing_user_data.get("features", []),
            "news": existing_user_data.get("news", [])
        }

        save_json(output_path, ordered_user_data)

    print(f"{len(users)} users successfully updated in '{output_dir}'")
