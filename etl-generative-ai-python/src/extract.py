import json
import pandas as pd
from config.config import RAW_DATA, MOCK_USERS_DIR


def extract_users():
    """
    Extract users using CSV and mocked JSON files.
    """
    df = pd.read_csv(RAW_DATA)
    user_ids = df["UserID"].tolist()

    users = []

    for user_id in user_ids:
        file_path = f"{MOCK_USERS_DIR}/user_{user_id}.json"
        with open(file_path, "r", encoding="utf-8") as f:
            users.append(json.load(f))

    return users
