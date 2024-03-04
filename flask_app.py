import random

from flask import Flask, jsonify, render_template

from philosophical_phrases import philosophical_phrases

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_phrase")
def get_phrase():
    # Get a random philosophical phrase
    random_entry = random.choice(philosophical_phrases)

    # Return the phrase as JSON
    return jsonify(phrase=random_entry["phrase"], author=random_entry["author"])


if __name__ == "__main__":
    app.run(debug=True)
