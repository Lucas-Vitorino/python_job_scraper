import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print("Erro ao acessar o site")
        return None

    


def parse_jobs(html):
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.find_all("div", class_="card-content")

    job_list = []

    for job in jobs:
        title_tag = job.find("h2", class_="title")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        company_tag = job.find("h3", class_="company")
        company = company_tag.get_text(strip=True) if company_tag else "N/A"

        location_tag = job.find("p", class_="location")
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

        apply_button = job.find("a", string="Apply")
        link = apply_button["href"] if apply_button else "N/A"

        job_data = {
            "title":title,
            "company":company,
            "location":location,
            "link":link
        }
        job_list.append(job_data)
    return job_list

def save_to_csv(jobs_list,filename):
    with open("jobs.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title","company", "location", "link"])
        writer.writeheader()
        writer.writerows(job_list)  
    

def main():
    url = "https://realpython.github.io/fake-jobs/"
    html = get_html(url)

    if html:
        jobs = parse_jobs(html)
        save_to_csv(jobs, "jobs.csv")
        print(f"{len(jobs)} vagas salvas com sucesso em jobs.csv")


if __name__ == "__main__":
    main()

