# Explorando IA Generativa em um Pipeline de ETL com Python

**Autor:** Raissa Santos Feitosa  
**GitHub:** [raissa-sf](https://github.com/raissa-sf)  
**LinkedIn:** [Raissa Santos Feitosa](https://www.linkedin.com/in/raissa-santos-feitosa-73485b1a3/)

## Descrição
Este projeto é um desafio do **Santander 2025 – Ciência de Dados com Python**, onde construí um pipeline de ETL que:

1. **Extrai** dados de usuários a partir de CSV e arquivos JSON mockados;
2. **Transforma** os dados gerando mensagens de marketing personalizadas usando templates;
3. **Carrega** os dados processados em arquivos JSON, mantendo histórico e IDs únicos das mensagens.

O objetivo é demonstrar o uso de Python para manipulação de dados, criação de pipelines ETL e simulação de personalização de marketing.

---

## Contexto / Ajustes do Projeto

A proposta inicial do desafio envolvia consumir a **API do Santander Dev Week 2023** para extrair os dados dos usuários e utilizar **IA Generativa (ChatGPT)** para criar mensagens de marketing personalizadas.  

No entanto, a API estava fora do ar durante o desenvolvimento. Para contornar isso, fiz as seguintes alterações:

- Substituí a API por **JSON mockados** armazenados localmente para simular os dados dos usuários;
- As mensagens de marketing foram geradas a partir de **templates prontos** no arquivo `templates.json`;
- O pipeline mantém a lógica de ETL, controle de IDs e histórico das mensagens, mantendo o objetivo de **personalização de marketing**.

Isso garante que o projeto ainda demonstre **processamento de dados, modularização e lógica de ETL**, mesmo sem consumir a API externa.

---

## Estrutura do Projeto
```
etl-generative-ai-python/
├─ config/
│  └─ config.py   
├─ data/
│  ├─ raw/                 # CSV com IDs de usuários
│  ├─ mock/users/          # JSONs mockados dos usuários
│  └─ processed/           # Usuários processados + message_ids.json
├─ src/
│  ├─ extract.py
│  ├─ transform.py
│  ├─ load.py
│  ├─ utils.py
├─ main.py              # Script principal do ETL
├─ requirements.txt
└─ README.md
```
---

## Funcionalidades

- **Extract:** Lê o CSV com IDs dos usuários e carrega os dados de cada usuário a partir de JSON mockado.
- **Transform:** Gera mensagens de marketing personalizadas para cada usuário, evitando duplicação e incrementando IDs globalmente.
- **Load:** Salva os usuários processados em JSON na pasta `data/processed/`, garantindo que `news` fique abaixo de `features` e mantendo histórico de mensagens.
- **Controle de IDs:** Armazena o último ID usado em `message_ids.json` para manter consistência em execuções futuras.

---

## Observações

 - Todos os comentários no código estão em inglês, mas o README está em português para maior clareza.

 - O pipeline pode ser rodado várias vezes; novas mensagens são adicionadas sem sobrescrever as antigas.

---
## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/raissa-sf/etl-generative-ai-santander.git
cd etl-generative-ai-python
```

2. Crie um ambiente virtual e instale dependências:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

3. Rode o pipeline:
```bash
python main.py
```

4. Confira os arquivos processados em:
```
data/processed/
├─ user_1.json
├─ user_2.json
├─ ...
└─ message_ids.json
```
# Exemplo do JSON processado (terminal)

No terminal, você verá cada usuário com suas mensagens de marketing personalizadas, seguindo a ordem de campos:

id → name → account → card → features → news

```
{
  "id": 1,
  "name": "Marcos Silva",
  "account": {
    "id": 1,
    "number": "00001-1",
    "agency": "0001",
    "balance": 0.0,
    "limit": 10000.0
  },
  "card": {
    "id": 1,
    "number": "**** **** **** 1231",
    "limit": 1500.0
  },
  "features": [],
  "news": [
    {
      "id": 7,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Cada passo financeiro conta, Marcos Silva. Não deixe para amanhã o que você pode investir hoje!"  
    }
  ]
}
```

# Exemplo do JSON salvo em processed/

O pipeline acrescenta novas mensagens sem sobrescrever as antigas. Cada mensagem recebe um ID único, armazenado em message_ids.json.
```
{
  "id": 1,
  "name": "Marcos Silva",
  "account": {
    "id": 1,
    "number": "00001-1",
    "agency": "0001",
    "balance": 0.0,
    "limit": 10000.0
  },
  "card": {
    "id": 1,
    "number": "**** **** **** 1231",
    "limit": 1500.0
  },
  "features": [],
  "news": [
    {
      "id": 1,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Planejar seu futuro nunca foi tão importante, Marcos Silva. Invista hoje!"
    },
    {
      "id": 6,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Cada passo financeiro conta, Marcos Silva. Não deixe para amanhã o que você pode investir hoje!"
    },
    {
      "id": 11,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Planejar seu futuro nunca foi tão importante, Marcos Silva. Invista hoje!"
    }
  ]
}
```

---

## Conclusão

Este projeto demonstra como montar um pipeline de ETL completo em Python, envolvendo:

- Extração de dados (CSV + JSONs mockados)
- Transformação com geração de mensagens personalizadas
- Carregamento mantendo histórico e ordem de campos compatível com APIs

Apesar da proposta inicial ser consumir a API do Santander Dev Week 2023 e gerar mensagens com IA, a solução adotada mantém o propósito do desafio utilizando **dados mockados** e templates de mensagens.  

O pipeline é replicável, escalável e pode ser adaptado para consumir APIs reais futuramente, mantendo a mesma lógica de ETL e personalização de mensagens.

---

## Referências

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)  
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)  
- [Santander 2025 - Ciência de Dados com Python](https://digitalinnovation.one)

