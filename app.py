from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route("/")
def route():
    return "Hello, world!"

@app.route("/get_user/", methods=['GET'])
def get_user():
    email = request.args.get('email')
    column = request.args.get('column')
    
    if email:
        print(f'\nEmail para verificar: {email}')
        user = database.get_user(email)

        if column:
            coluna = user.get(column)
            return jsonify(coluna), 200

        return jsonify(user), 200

    return "Email not provided", 400

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    print(f'\nDados recebidos')
    
    if not data:
        return "Bad Request", 400
    
    nome = data.get('nome')
    email = data.get('email')
    idade = data.get('idade')
    salario = data.get('salario')
    if salario:
        values = {nome, email, idade, salario}
    else:
        values = {nome, email, idade}
        
    database.create_user(values)
    
    return jsonify(data), 201

if __name__ == ("__main__"):
    app.run()