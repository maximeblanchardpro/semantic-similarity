import json
import re
from nltk.corpus import stopwords

def extract_apidae_corpus(path: str) -> list:
    corpus = []
    with open(path, 'r') as f:
        pois = json.load(f)['objetsTouristiques']

    for poi in pois:
        try:
            poi = {
                "id": poi["id"],
                "document": poi["nom"]["libelleFr"] + " " + poi["type"] + " " + poi["presentation"]["descriptifCourt"]["libelleFr"]
                }

            corpus.append(poi)

        except KeyError:
            print("no description")

    return corpus

def remove_punctuation(document: str):
    text = document.lower()

    r = re.compile("[-!,;_.(){}]")
    document = r.sub(string=document, repl=" ")

    r = re.compile("  ")
    document = r.sub(string=document, repl=" ")

    return document

def remove_stopwords(document: str):
    try:
        document = " ".join([word for word in document.split(" ") if word not in stopwords.words('french')])
        return document

    except LookupError:
        import nltk
        nltk.download('stopwords')
        remove_stopwords(document)

def clean_document(document: str):
    document = remove_punctuation(document)
    document = remove_stopwords(document)

    return document