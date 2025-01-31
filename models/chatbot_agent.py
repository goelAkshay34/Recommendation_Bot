from transformers import pipeline

class ChatbotAgent:
    def __init__(self, model_name="google/flan-t5-large"):
        """
        Initializes the ChatbotAgent with a pre-trained model.
        Args:
            model_name (str): Name of the pre-trained model to use.
        """
        self.chatbot = pipeline("text2text-generation", model=model_name)

    def query(self, user_query):
        """
        Processes a user query and generates a response.
        Args:
            user_query (str): The user's question or input.
        Returns:
            str: The chatbot's response.
        """
        try:
            # Handle empty queries
            if not user_query or user_query.strip() == "":
                return "I'm sorry, I couldn't understand that."

            # Generate a response using the model
            response = self.chatbot(user_query, max_length=100)
            if response and isinstance(response, list) and len(response) > 0:
                generated_text = response[0].get("generated_text", "").strip()
                if generated_text:
                    return generated_text
                else:
                    return "I'm sorry, I couldn't understand that."
            else:
                return "I'm sorry, I couldn't understand that."
        except Exception as e:
            return f"An error occurred: {str(e)}"
