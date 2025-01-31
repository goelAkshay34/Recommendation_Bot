from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self):
        self.content_embeddings = {}  # Stores embeddings for learning content

    def add_content(self, content_id, content_text, nlp_model):
        """
        Adds learning content to the recommendation engine.
        Args:
            content_id (str): Unique ID for the content.
            content_text (str): Textual description of the content.
            nlp_model (NLPModel): NLP model to generate embeddings.
        """
        self.content_embeddings[content_id] = nlp_model.get_text_embedding(content_text)

    def recommend(self, user_embedding):
        """
        Recommends content based on user embedding.
        Args:
            user_embedding (list): User's interest embedding.
        Returns:
            list: Sorted list of recommended content IDs.
        """
        similarities = {}
        for content_id, content_embedding in self.content_embeddings.items():
            similarity = cosine_similarity([user_embedding], [content_embedding])[0][0]
            similarities[content_id] = similarity
        sorted_recommendations = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_recommendations]
