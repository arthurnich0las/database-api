from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route("/")
def route():
    return "Hello, world!"

@app.route("/get-user/<dbname>/<email>")
def get_user(dbname, email):
    user = database.get_user(dbname, email)
    user_data = jsonify(user[0])
    return user_data, 200

if __name__ == ("__main__"):
    app.run()