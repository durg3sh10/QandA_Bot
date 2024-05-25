from transformers import AutoTokenizer, AutoModel
import torch

class EmbeddingModel:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def get_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()

def get_embeddings(texts, model_name='sentence-transformers/all-MiniLM-L6-v2'):
    model = EmbeddingModel(model_name)
    embeddings = [model.get_embedding(text) for text in texts]
    return embeddings
