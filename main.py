from src.extract import extract_users
import json


if __name__ == "__main__":
    users = extract_users(
        csv_path="data/raw/SDW2023.csv",
        mock_dir="data/mock/users"
    )

    print(f"{len(users)} usuários extraídos com sucesso\n")
    print(json.dumps(users, indent=2, ensure_ascii=False))
