# Ob zagonu program ustvari tabelo s spletne strani https://disfold.com/world/companies/.
# Te podatke bomo uporabili, ko bomo prikazali podatke o podjetjih, tj. s čem se ukvarjajo, na katerem področju.

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://disfold.com/world/companies/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    rows = table.find_all("tr")
    data = []

    for row in rows:
        cells = row.find_all(["th", "td"])
        if cells:
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)

    # maksimalno število stolpcev
    max_columns = max(len(row) for row in data)

    for i in range(len(data)):
        if len(data[i]) < max_columns:
            data[i] += [""] * (max_columns - len(data[i]))

    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_csv("podjetja_podrobnosti.csv", index=False)
    print("CSV datoteka je ustvarjena.")