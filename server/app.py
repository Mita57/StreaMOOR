import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from .models import SQLModel
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('/login', methods=['POST'])
def login():
    """
    Gets the data from the login form and authorizes the input

    Returns: JSON with auth result info
    """
    post_data = request.get_json()
    user = SQLModel.get_by_attrs('email, password', 'email', (post_data.get('email')))
    if post_data.get('pwrd') == user[0][1]:
        return jsonify(style='color:lightgreen', info='Вход выполнен', flag=True)
    else:
        return jsonify(style='color:red', info='Неправильное имя пользователя или пароль', flag=False)


@app.route('/register', methods=['POST'])
def register():
    """
    Inserts the information about new user unto the database

    Returns:
        JSON with the result
    """
    post_data = request.get_json()
    if SQLModel.get_by_attrs('email, password', 'email', (post_data.get('email'))):
        return jsonify(info='Данный пользователь уже зарегестрирован')
    else:
        date = datetime.date.day + '/' + datetime.date.month + '/' + datetime.date.year
        SQLModel.insert((post_data.get('nickname'), post_data.get('email'), post_data.get('password'), None,
                         date, None, post_data.get('birthDate'), 'user', False))


if __name__ == '__main__':
    app.run(debug=True)
