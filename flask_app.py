from flask import Flask, render_template, request, jsonify
import random
from philosophical_phrases import philosophical_phrases

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_phrase')
def get_phrase():
    # Get a random philosophical phrase
    random_entry = random.choice(philosophical_phrases)

    # Return the phrase as JSON
    return jsonify(phrase=random_entry['phrase'], author=random_entry['author'])

@app.route('/get_ip')
def get_ip():
    # Function to get the user's IP address
    def get_real_ip():
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            ip = request.remote_addr
        return ip

    # Get the public IP address
    user_ip = get_real_ip()

    # Append the IP to a file
    with open('user_ips.txt', 'a') as file:
        file.write(user_ip + '\n')

    # Return the IP as JSON
    return jsonify(ip=user_ip)

if __name__ == '__main__':
    app.run(debug=True)
