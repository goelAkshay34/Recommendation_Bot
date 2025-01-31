import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "../data/learning_data.db")
MODEL_PATH = "distilbert-base-uncased"  # Pre-trained Hugging Face model
