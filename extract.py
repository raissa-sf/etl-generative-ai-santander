import pandas as pd
import json
from pathlib import Path


def extract_users(csv_path: str, mock_dir: str) -> list:
    """
    Extrai dados de usuários a partir de arquivos JSON mockados,
    simulando a resposta da API original.

    Args:
        csv_path (str): Caminho do CSV com a coluna 'user_id'
        mock_dir (str): Diretório onde estão os JSONs mockados

    Returns:
        list: Lista de dicionários com os dados brutos dos usuários
    """
    df = pd.read_csv(csv_path)
    user_ids = df["UserID"].tolist()

    users = []

    for user_id in user_ids:
        file_path = Path(mock_dir) / f"user_{user_id}.json"

        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                users.append(json.load(file))
        else:
            print(f"[WARN] Mock do usuário {user_id} não encontrado.")

    return users
