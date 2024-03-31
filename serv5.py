from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Neha:password5@cluster5.pvdodhn.mongodb.net/database5?retryWrites=true&w=majority&appName=Cluster5"

mongodb_client = PyMongo(app)
db = mongodb_client.db
print(db)
if db is None:
    print("not connected")
else:
    print("connected to mongo")
CORS(app)   #to get data from frontend(cross platform)
@app.route("/", methods=["GET"])
def get_all_todo_items():
    return "todos"
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)