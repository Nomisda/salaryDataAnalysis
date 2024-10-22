import requests
from bs4 import BeautifulSoup
import csv
from displayData import *
from extractionFunktions import * 

data = []
#Seiten iterieren
for x in range(20,41):

    url = "https://www.fachinformatiker.de/topic/114321-wie-viel-verdient-ihr/page/{index}/".format(index = x)


    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    posts = soup.find_all(['div'], {'data-role': 'commentContent'})
    posts.extend(soup.find_all(['div'], {'class' : "ipsQuote_contents"}))


    for post in posts:
        post_text = post.get_text(separator="\n") 

        experience_line = None

        for line in post_text.splitlines():
            if "Berufserfahrung" in line or "Erfahrung" in line or "Berufsjahre" in line:
                experience_line = line.strip()
                break
        
        salary_line = None

        for line in post_text.splitlines():
            if "Gesamtjahresbrutto" in line or "Gesamtbrutto" in line or "brutto" in line:
                salary_line = line.strip()
                break

        # speichern wenn Gehalt und Erfahrung extracted werden konnten
        if experience_line and salary_line:
            data.append({
                'Berufserfahrung': experience_line,
                'Gehalt': salary_line
            })

print("length full data:")
print(len(data))
extracted_data = []

for entry in data:
    experience = extract_experience(entry["Berufserfahrung"])
    salary = extract_salary(entry["Gehalt"])

    if experience is not None and salary is not None:
        extracted_data.append({'Berufserfahrung': experience, 'Gesamtjahresbrutto': salary})

computeLoehne(extracted_data)

