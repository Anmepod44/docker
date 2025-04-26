# dependencies : Flask
from flask import Flask

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World! This is the Flask app running in a Docker container.'

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)