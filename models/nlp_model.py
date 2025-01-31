from transformers import pipeline
import string

class NLPModel:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.model = pipeline("feature-extraction", model=model_name)

    def preprocess_text(self, text):
        """
        Preprocesses the input text.
        Args:
            text (str): Input text.
        Returns:
            str: Cleaned text.
        """
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    def get_text_embedding(self, text):
        """
        Generates an embedding for the given text.
        Args:
            text (str): Input text.
        Returns:
            list: Embedding vector.
        """
        cleaned_text = self.preprocess_text(text)
        result = self.model(cleaned_text)
        return result[0][0]  # Use the first token's embedding
