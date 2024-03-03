import datetime
import random

from flask import Flask, jsonify, render_template, request

from philosophical_phrases import philosophical_phrases

app = Flask(__name__)


# Function to log IP addresses to a text file
def log_ip(ip_address):
    with open("ip_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {ip_address}\n")


@app.route("/")
def index():
    ip_address = request.remote_addr
    log_ip(ip_address)
    return render_template("index.html")


@app.route("/get_phrase")
def get_phrase():
    # Get a random philosophical phrase
    random_entry = random.choice(philosophical_phrases)

    # Return the phrase as JSON
    return jsonify(phrase=random_entry["phrase"], author=random_entry["author"])


if __name__ == "__main__":
    app.run(debug=True)
