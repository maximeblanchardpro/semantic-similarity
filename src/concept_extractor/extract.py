from sentence_transformers import SentenceTransformer

def init_model(model_name="intfloat/multilingual-e5-small") -> SentenceTransformer:
    try:
        model = SentenceTransformer(f"./models/{model_name}")

    except FileNotFoundError:
        model = SentenceTransformer(model_name)

    return model

def score_concepts(document: str, model: SentenceTransformer, concepts: list):
    document_embedding = model.encode_query(document)
    concepts_embedding = model.encode_document(concepts)

    scores = model.similarity(document_embedding, concepts_embedding)[0]

    return scores