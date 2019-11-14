import json
from flask import Flask, jsonify, request
from .models import SQLModel

app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()
    user = SQLModel.get_by_id((post_data.get('email')), 'email, password')
    if post_data.get('pwrd') == user[0][1]:
        return jsonify(style='color:lightgreen', info='Вход выполнен', flag=True)
    else:
        return jsonify(style='color:red', info='Неправильное имя пользователя или пароль', flag=False)








if __name__ == '__main__':
    app.run(debug=True)
