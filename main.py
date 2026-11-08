from src.data_prep.textual import extract_apidae_corpus, clean_document
from src.concept_extractor.extract import init_model, score_concepts
import json

corpus = extract_apidae_corpus(path="data/pois-uc1.json")
concepts = json.load(open("data/concepts.json", "r"))

model = init_model(model_name="intfloat/multilingual-e5-small")

for desc in corpus:
    desc["document"] = clean_document(desc["document"])
    scores = score_concepts(document=desc["document"], model=model, concepts=concepts)

    print(desc["document"])
    for index in scores.argsort(descending=True):
        print(f"{scores[index]:.4f}: {concepts[index]}")