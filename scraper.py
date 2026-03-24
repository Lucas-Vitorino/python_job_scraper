import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all("div", class_="card-content")

    job_list = []

    for job in jobs:
    #título
        title_tag = job.find("h2", class_="title")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

    #Empresa
        company_tag = job.find("h3", class_="company")
        company = company_tag.get_text(strip=True) if company_tag else "N/A"

    #Localização
        location_tag = job.find("p", class_="location")
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

    #Link
        apply_button = job.find("a", string="Apply")
        link = apply_button["href"] if apply_button else "N/A"

        job_data = {
            "title":title,
            "company":company,
            "location":location,
            "link":link
        }

        job_list.append(job_data)
    with open("jobs.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title","company", "location", "link"])

        writer.writeheader()
        writer.writerows(job_list)
        
    print("Arquivo jobs.csv foi criado com sucesso!")    
    
else:
    print("Erro ao acessar o site")

