# S tem programom pridobimo podatke za kasnejšo analizo
# Za zagon te funkcije najprej moramo v Terminal-u zagnati: pip install request pandas
 
import pandas as pd
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "referer": "https://www.forbes.com/global2000/",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}

cookies = {
    "notice_behavior": "expressed,eu",
    "notice_gdpr_prefs": "0,1,2:1a8b5228dd7ff0717196863a5d28ce6c",
}

api_url = "https://www.forbes.com/forbesapi/org/global2000/2025/position/true.json?limit=2000"
response = requests.get(api_url, headers=headers, cookies=cookies).json()

sample_table = [
    [
        item["organizationName"],
        item["country"],
        item["revenue"],
        item["profits"],
        item["assets"],
        item["marketValue"]
    ] for item in
    sorted(response["organizationList"]["organizationsLists"], key=lambda k: k["position"])
]

df = pd.DataFrame(sample_table, columns=["Ime podjetja", "Država", "Prodaja", "Dobiček", "Sredstva", "Tržna vrednost"])
df.to_csv("podatki_2025.csv", index=False)
