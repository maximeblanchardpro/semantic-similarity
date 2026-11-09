from src.data_prep.textual import extract_apidae_corpus, clean_document
from src.data_ingest.ingest_apidae import ingest_apidae
from src.semantic.extract import init_model, score_similarity

ingest_apidae()

corpus = extract_apidae_corpus(path="data/pois.json")

clean_corpus = []

for doc in corpus:
    doc["document"] = clean_document(doc["document"])

poi = corpus.pop(0)

print(poi)

model = init_model(model_name="intfloat/multilingual-e5-small")
similarities = score_similarity(documents=[poi], corpus=corpus, model=model)

print(poi["nom"])

results = []

print(f"{poi["description"]: <30}")

for idx_j, poi in enumerate(corpus):
    poi["score"] = similarities[0][idx_j]
