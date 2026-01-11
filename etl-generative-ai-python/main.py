"""
ETL Pipeline for Santander 2025 Data Science Challenge
Stage: Extract -> Transform
This script extracts user data from mocked JSON files,
applies the transformation to generate personalized marketing messages,
and prints the results.
"""

from src.extract import extract_users
from src.transform import generate_marketing_news
import json

if __name__ == "__main__":

    # Extract user data from CSV and mocked JSON files
    users = extract_users(
        csv_path="data/raw/SDW2023.csv",
        mock_dir="data/mock/users"
    )
    print(f"{len(users)} users successfully extracted.\n")

    # Generate personalized marketing messages for each user
    users_with_news = generate_marketing_news(users)

    # Print transformed users with 'news' field filled
    print("Transformed user data with personalized news:\n")
    print(json.dumps(users_with_news, indent=2, ensure_ascii=False))
