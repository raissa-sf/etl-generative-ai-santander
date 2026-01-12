import os
import random
from config.config import TEMPLATES_FILE, MESSAGE_ID_FILE
from .utils import load_json, save_json


def generate_marketing_news(users: list, template_path=TEMPLATES_FILE, id_file=MESSAGE_ID_FILE) -> list:
    """
    Generates personalized marketing messages for each user,
    adding new messages and incrementing message IDs globally.

    Args:
        users (list): List of user dictionaries with user data
        template_path (str): Path to JSON file with message templates
        id_file (str): Path to JSON file storing last used message ID

    Returns:
        list: Users list with new 'news' messages appended
    """

    # Load message templates
    templates = load_json(template_path)
    if not templates:
        raise ValueError(f"No templates found in {template_path}")

    # Shuffle templates to avoid always sending the same order
    random.shuffle(templates)

    # Load last used message ID
    last_id_data = load_json(id_file)
    last_id = last_id_data.get("last_id", 0)

    # Assign messages to users
    for user, template in zip(users, templates):
        name = user.get("name", "Customer")
        last_id += 1  # Increment global ID
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
    save_json(id_file, {"last_id": last_id})

    return users
