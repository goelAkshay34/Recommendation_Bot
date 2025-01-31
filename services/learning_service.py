from models.nlp_model import NLPModel
from models.recommendation import RecommendationEngine
from utils.database_utils import DatabaseUtils
from sklearn.metrics.pairwise import cosine_similarity

class LearningService:
    def __init__(self):
        self.db_utils = DatabaseUtils()
        self.nlp_model = NLPModel()
        self.recommendation_engine = RecommendationEngine()
        self._load_content()

    def _load_content(self):
        """
        Loads learning content into the recommendation engine.
        """
        contents = self.db_utils.get_all_content()
        for content in contents:
            self.recommendation_engine.add_content(
                content_id=content["id"],
                content_text=content["description"],
                nlp_model=self.nlp_model
            )
    
    def get_recommendations(self, username):
        """
        Gets personalized recommendations for a user.
        Args:
            username (str): Username.
        Returns:
            list: List of dictionaries containing content ID and description.
        """
        user = self.db_utils.get_user(username)
        if not user or not user["interests"]:
            return []  # Return an empty list if no interests are available

        user_embedding = self.nlp_model.get_text_embedding(user["interests"])
        similarities = {}
        for content_id, content_embedding in self.recommendation_engine.content_embeddings.items():
            similarity = cosine_similarity([user_embedding], [content_embedding])[0][0]
            similarities[content_id] = similarity

        # Sort by similarity score (descending order)
        sorted_recommendations = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

        # Fetch content details for the top recommendations
        recommended_content = []
        for content_id, _ in sorted_recommendations:
            content = self.db_utils.get_content_by_id(content_id)
            if content:
                recommended_content.append({
                    "id": content["id"],
                    "description": content["description"]
                })

        return recommended_content
