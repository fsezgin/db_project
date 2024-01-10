from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

app = Flask(__name__)

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["library"]
    return db

@app.route("/")
def ping_server():
    return "Hellomm"

@app.route("/books")
def fetch_books():
    db = get_db()
    # Now creating a Cursor instance 
    # using find() function 
    cursor = db.library.find() 
  
    # Converting cursor to the list  
    # of dictionaries 
    list_cur = list(cursor) 
    
    # Converting to the JSON 
    json_data = dumps(list_cur, indent = 2) 
    return json_data 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)