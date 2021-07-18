import os.path
import json
from flask import Flask
import datetime

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "res")

format_time = "%d %m %Y %H:%M:%S"

@app.route('/')
def index():
    with open(os.path.join(RESOURCE_DIR, "name.json")) as file:
        return f"{json.loads(file.read()).get('current_time')}:{datetime.datetime.now().strftime(format_time)}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
