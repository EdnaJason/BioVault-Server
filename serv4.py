from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://EdnaJason:password4@cluster4.21eeuoa.mongodb.net/database4?retryWrites=true&w=majority&appName=Cluster4"

mongodb_client = PyMongo(app)
db = mongodb_client.db
print(db)
if db is None:
    print("not connected")
else:
    print("conectd to mongo")
CORS(app)
@app.route("/", methods=["GET"])
def get_all_todo_items():
    return "todos"
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)