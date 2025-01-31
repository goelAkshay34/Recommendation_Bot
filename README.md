# Personalized Learning Platform

[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  


A web-based platform that provides personalized learning content recommendations and an interactive chatbot.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

---

## Overview

The **Personalized Learning Platform** helps users discover learning materials tailored to their interests. It uses NLP techniques and a recommendation engine to provide personalized suggestions. An interactive chatbot assists users with questions.

---

## Features

- **User Authentication**: Register, log in, and manage user interests.
- **Personalized Recommendations**: Content recommendations based on user interests using cosine similarity.
- **Interactive Chatbot**: Real-time responses powered by pre-trained NLP models like `google/flan-t5-large`.
- **Dashboard**: Displays recommended content and chatbot interface.

---

## Installation

### Prerequisites
- Python 3.10+
- Pipenv (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personalized-learning-platform.git
   cd personalized-learning-platform

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Initialize the database:
    ```bash
    python utils/database_utils.py
4. Run the application:
    ```bash
    python app.py
5. Access the platform at http://127.0.0.1:5000/ .

# Usage
1. Register/Login : Create an account or log in with your credentials.
2. Explore Recommendations : View personalized content based on your interests.
3. Chatbot : Ask questions and get real-time answers.
4. Logout : End your session.

# Technologies Used
- Backend : Flask, SQLite
- NLP Models : Hugging Face Transformers (sentence-transformers, google/flan-t5-large)
- Frontend : HTML, CSS, JavaScript

# Future Enhancements
- Integrate external APIs for dynamic content fetching.
- Add collaborative filtering for better recommendations.
