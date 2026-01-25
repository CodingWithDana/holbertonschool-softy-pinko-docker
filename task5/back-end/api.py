from flask import Flask
from flask_cors import CORS  # install this CORS module to allow our backend to accept cross-origin requests from our front end

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)