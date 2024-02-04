from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Placeholder for your routes and other configurations
# Add your routes, database configurations, and other settings below

@app.route('/')
def hello():
    return 'Hello, Pizza App!'

if __name__ == '__main__':
    app.run(debug=True)
