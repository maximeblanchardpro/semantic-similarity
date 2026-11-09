import json
import requests

def ingest_apidae():
    base_url = 'https://api.apidae-tourisme.com/api/v002/recherche/list-objets-touristiques/?query='

    query = {
        "projetId":9657,
        "apiKey":"",
        "selectionIds":[211884,211888,211889,211890,211891,211892,211905,211906,211908,211911,211914,211999],
        "count":100,
        "first":0
    }

    r = requests.get(base_url + json.dumps(query))

    with open("data/pois.json", "w") as f:
        f.write(json.dumps((r.json()), indent=2))