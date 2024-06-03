from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Настройка подключения к MongoDB
client = MongoClient("mongo", 27017)
db = client.test_database

@app.route('/')
def index():
    return "HI its me mongo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
