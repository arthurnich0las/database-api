# database-api
API feita usando o micro framework Flask, integrando e interagindo com um banco de dados MySQL externo, podendo acessar dados relacionados a usuarios e modificá-los

# Instalação
Para começar, é necessários instalar as bibliotecas necessárias, que estão contidas em "requirements.txt"

Comando para instalar:
pip install -r requirements.txt

# Rodar
Para rodarmos a API, é necessário rodar o programa app.py, usando o comando:
python app.py

Ao executar, a API começará a escutar requests no localhost (http://127.0.0.1:5000/)

# Recomendações
Para melhor interação com a API, recomendado usar Postman para criar requests tanto GET quanto POST

# Requests
Foi implementado requests para lidarem com o CRUD básico de um banco de dados relacional (MySQL), e as possiveis requests são:

http://127.0.0.1:5000/create-user/

    Cria um usuário no banco de dados, baseado no json enviado, com os dados a serem inseridos no formato:
    {
        "nome": "",
        "email": "",
        "idade": "",
        "salario": ""
    }

http://127.0.0.1:5000/read-user/<email>
    
    Retornará os dados do usuario do email em questão.

http://127.0.0.1:5000/update-user/<email>

    Atualizará os dados do usuário do email em questão, se baseando no json enviado, no formato:
    {
        "nome": "",
        "idade": "",
        "salario": ""
    }

http://127.0.0.1:5000/delete-user/<email>

    Deletará o usuário do email em questão.