from flask import Flask, jsonify, render_template
import os
import random

app = Flask(__name__)

quotes = [
    "Keep it simple!",
    "DevOps is culture and automation.",
    "Infrastructure as Code rocks.",
    "Containers are lightweight magic.",
    "Code once, deploy everywhere."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    app_name = os.getenv("APP_NAME", "Flask Microservice")
    db_host = os.getenv("DB_HOST", "localhost")

    message = {
        "app": app_name,
        "database_host": db_host,
        "quote_of_the_day": random.choice(quotes),
        "message": "Welcome to the creative and simple Flask microservice!"
    }
    return jsonify(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
