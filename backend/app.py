from flask import Flask, render_template
from dotenv import load_dotenv
import os

#load environmnet variables from .env file
load_dotenv()

app = Flask(
    __name__,
    template_folder='../frontend/pages',
    static_folder='../frontend'
)

# Load secret key from environment
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'my-secret-key')

@app.route('/')
def home():
    return render_template('index.html')

# Run the app

if __name__ == '__main__':
    app.run(debug=True, port=5000)