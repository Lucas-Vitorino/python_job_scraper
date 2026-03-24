# Python Job Scraper

Scraper em Python que coleta vagas do site Fake Python Jobs, extraindo título, empresa, localização e link. Os dados são organizados e exportados para CSV.

## 🚀 Tecnologias utilizadas

- Python
- Requests
- BeautifulSoup (bs4)
- CSV

## 📊 Dados extraídos

- Título da vaga
- Empresa
- Localização
- Link da vaga

## 📁 Estrutura do projeto
python_job_scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/Lucas-Vitorino/python_job_scraper.git
cd python_job_scraper
2. Criar ambiente virtual
python -m venv venv
3. Ativar ambiente

## ⚙️ Windows

venv\Scripts\activate

## ⚙️ Mac

source venv/bin/activate
4. Instalar dependências
pip install -r requirements.txt
5. Executar o projeto
python scraper.py
📄 Saída

O script gera o arquivo:

jobs.csv

com todas as vagas coletadas.

📌 Observações
O arquivo jobs.csv é gerado automaticamente e não deve ser versionado.
Projeto desenvolvido para prática de web scraping e manipulação de dados.
🔮 Próximas melhorias
Refatoração em funções
Exportação para JSON
Filtros por palavra-chave
Melhor tratamento de erros

---

Depois disso, no terminal:

```bash
git add README.md
git commit -m "docs: add README"
git push
