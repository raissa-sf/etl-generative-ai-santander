import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA = os.path.join(BASE_DIR, "data/raw/SDW2023.csv")
MOCK_USERS_DIR = os.path.join(BASE_DIR, "data/mock/users")
PROCESSED_DIR = os.path.join(BASE_DIR, "data/processed")
TEMPLATES_FILE = os.path.join(BASE_DIR, "data/templates/messages.json")
MESSAGE_ID_FILE = os.path.join(PROCESSED_DIR, "message_ids.json")

