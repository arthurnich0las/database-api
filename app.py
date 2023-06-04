from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route("/")
def route():
    return "Hello, world!"

@app.route("/create-user/", methods=["POST"])    # CREATE
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
        values = [nome, email, idade, salario]
    else:
        values = [nome, email, idade]
        
    database.create_user(values)
    
    return jsonify(data), 201

@app.route("/read-user/<email>/", methods=['GET'])   # READ
def get_user(email):
    column = request.args.get('column')
    
    if email:
        status_email = database.check_user(email)
        if status_email != 200:
            return 'Email does not exist in our databases' 
        
        print(f'\nEmail para verificar: {email}')
        user = database.get_user(email)

        if column:
            coluna = user.get(column)
            return jsonify(coluna), 200

        return jsonify(user), 200

    return "Email not provided", 400

@app.route("/update-user/<email>/", methods=['PUT'])
def update_user(email):
    data = request.get_json()
    print(f'\nDados recebidos: {data}')
    
    if not data:
        return "Data not provided", 400
    
    status_email = database.check_user(email)
    
    if status_email == 200:
        fields = []
        values = []
        
        if 'nome' in data:
            fields.append('nome = %s')
            values.append(data['nome'])
        
        if 'idade' in data:
            fields.append('idade = %s')
            values.append(data['idade'])
        
        if 'salario' in data:
            fields.append('salario = %s')
            values.append(data['salario'])
        
        if not fields:
            return "No fields to update", 400
        
        query = "UPDATE usuarios SET " + ", ".join(fields) + " WHERE email = %s"
        values.append(email)
        print(f'Query de update: {query}')
        
        database.update_user(query, values)
        
        retorno = {
            "email": email,
            "status": "Updated"
        }
        
        return jsonify(retorno), 200
    else:
        return "User not found", 404
    

@app.route("/delete-user/<email>", methods=["DELETE"])     # DELETE
def delete_user(email):
    if not email:
        return "Email not provided", 400
    
    delete = database.delete_user(email)
    if delete == 200:
        dict = {
            "email": email,
            "status": "Deleted"
        }
        return jsonify(dict), 200
    elif delete == 400:
        return 'Email does not exist in our databases', 400
    
    else:
        return 'Not Found', 404

if __name__ == ("__main__"):
    app.run()