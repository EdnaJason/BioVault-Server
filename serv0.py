from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo
#from fpmatch import matching as m
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Edna:password0@cluster0.f7lin8b.mongodb.net/Database0?retryWrites=true&w=majority"

mongodb_client = PyMongo(app)
db = mongodb_client.db
#print(db)
if db is None:
    print("not connected")
else:
    print("conectd to mongo")
CORS(app)
@app.route("/", methods=["GET"])
def get_all_todo_items():
    kp1,kp2=[],[]
    desc1,desc2=[],[]
    score=m(kp1,desc1,kp2,desc2)
    return "todos"
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)