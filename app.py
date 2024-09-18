from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv

import os

load_dotenv()

app = Flask(__name__)

uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

# cluster -> databases -> collections -> document / query

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(client["BLEATH"].list_collection_names())
except Exception as e:
    print(e)

@app.route("/")
def hello_world():
    return render_template("index.html")

if (__name__ == "__main__"):
    app.run(debug=True)