import json
import random

def generate_marketing_news(users: list, template_path="data/templates/messages.json") -> list:
    """
    Generates personalized marketing messages for each user,
    ensuring each user receives a unique message.

    Args:
        users (list): List of dictionaries with user data
        template_path (str): Path to the JSON file with message templates

    Returns:
        list: Same list of users, but with the 'news' key filled
    """
    # Load templates from JSON file
    with open(template_path, "r", encoding="utf-8") as f:
        templates = json.load(f)

    # Ensure there are enough templates for all users
    if len(templates) < len(users):
        raise ValueError("Not enough templates for all users")

    # Shuffle templates to assign randomly
    random.shuffle(templates)

    # Assign one unique message per user
    for idx, (user, template) in enumerate(zip(users, templates), start=1):
        name = user.get("name", "Customer")
        message_text = template.format(name=name)

        message = {
            "id": idx,  # unique message id
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": message_text
        }

        # Add message to the user's 'news' list
        user["news"] = [message]

    return users
