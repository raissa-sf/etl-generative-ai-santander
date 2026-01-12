import json
import os
from config.config import PROCESSED_DIR


def load_users(users: list, output_dir: str = PROCESSED_DIR):
    """
    Saves each user with personalized news to a JSON file,
    appending new messages without overwriting existing ones
    and ensuring the JSON field order matches the Santander API.
    
    Order:
    id -> name -> account -> card -> features -> news
    """
    os.makedirs(output_dir, exist_ok=True)

    for user in users:
        user_id = user.get("id")
        output_path = os.path.join(output_dir, f"user_{user_id}.json")

        # Load existing user data if file already exists
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as file:
                existing_user_data = json.load(file)
        else:
            existing_user_data = {"news": []}

        # Merge existing news with new news (avoid duplicate IDs)
        existing_news_ids = {
            news_item["id"]
            for news_item in existing_user_data.get("news", [])
        }

        for new_message in user.get("news", []):
            if new_message["id"] not in existing_news_ids:
                existing_user_data.setdefault("news", []).append(new_message)

        # Update user attributes except 'news'
        for field_name, field_value in user.items():
            if field_name != "news":
                existing_user_data[field_name] = field_value

        # Explicitly control JSON field order
        ordered_user_data = {
            "id": existing_user_data.get("id"),
            "name": existing_user_data.get("name"),
            "account": existing_user_data.get("account"),
            "card": existing_user_data.get("card"),
            "features": existing_user_data.get("features", []),
            "news": existing_user_data.get("news", [])
        }

        # Save ordered user data
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(ordered_user_data, file, indent=2, ensure_ascii=False)

    print(f"{len(users)} users successfully updated in '{output_dir}'")
