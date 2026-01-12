import json
import random
import os
from config.config import TEMPLATES_FILE, MESSAGE_ID_FILE

def generate_marketing_news(users: list, template_path=TEMPLATES_FILE, id_file=MESSAGE_ID_FILE) -> list:
    """
    Generates personalized marketing messages for each user,
    adding new messages and incrementing message ids globally.

    Args:
        users (list): List of user dictionaries with user data
        template_path (str): Path to JSON file with message templates
        id_file (str): Path to JSON file storing last used message id

    Returns:
        list: Users list with new 'news' messages appended
    """
    # Load message templates
    with open(template_path, "r", encoding="utf-8") as f:
        templates = json.load(f)

    # Shuffle templates
    random.shuffle(templates)

    # Load last used message id
    if os.path.exists(id_file):
        with open(id_file, "r", encoding="utf-8") as f:
            last_id = json.load(f).get("last_id", 0)
    else:
        last_id = 0

    # Assign messages
    for user, template in zip(users, templates):
        name = user.get("name", "Customer")
        last_id += 1  # increment global id
        message_text = template.format(name=name)

        message = {
            "id": last_id,
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": message_text
        }

        # Append new message to user's existing news
        if "news" not in user:
            user["news"] = []
        user["news"].append(message)

    # Save updated last_id
    os.makedirs(os.path.dirname(id_file), exist_ok=True)
    with open(id_file, "w", encoding="utf-8") as f:
        json.dump({"last_id": last_id}, f)

    return users
