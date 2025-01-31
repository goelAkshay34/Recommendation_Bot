from flask import Flask, render_template, request, redirect, url_for, session
from services.user_service import UserService
from services.learning_service import LearningService
from models.chatbot_agent import ChatbotAgent

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For session management

# Initialize services
user_service = UserService()
learning_service = LearningService()
chatbot_agent = ChatbotAgent()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if user_service.authenticate(username, password):
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials"
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_username = request.form.get("new_username")
        new_password = request.form.get("new_password")
        interests = request.form.get("interests")

        # Check if the username already exists
        if user_service.get_user(new_username):
            return "Username already exists. Please choose a different one."

        # Hash the password (optional but recommended)
        hashed_password = new_password  # Replace with bcrypt or werkzeug.security for production

        # Add the new user to the database
        user_service.add_user(new_username, hashed_password, interests)
        return redirect(url_for("home"))
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("home"))
    username = session["username"]
    recommendations = learning_service.get_recommendations(username)
    return render_template("dashboard.html", username=username, recommendations=recommendations)

@app.route("/chat", methods=["POST"])
def chat():
    if "username" not in session:
        return redirect(url_for("home"))

    # Get the query from the request
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return {"response": "Invalid request. Please try again."}

        query = data["query"]
        print(f"User Query: {query}")  # Debugging statement

        # Validate the query
        if not query or query.strip() == "":
            return {"response": "Please enter a valid question."}

        # Pass the query to the chatbot
        response = chatbot_agent.query(query)
        print(f"Chatbot Response: {response}")  # Debugging statement
        return {"response": response}
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging statement
        return {"response": f"An error occurred: {str(e)}"}

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
