from flask import Flask
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    raise Exception('Okayy! Can you hack the console now?')
    return 'Hello from LPU!'

if __name__ == '__main__':
    app.run(debug=True)