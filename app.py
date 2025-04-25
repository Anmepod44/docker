# dependencies : Flask
from flask import Flask

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)