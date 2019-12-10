from flask import Flask, jsonify, request
from models import SQLModel
from models.subscriptions import Subsctiption
from models.users import User
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
async def login():
    """
    Gets the data from the login form and authorizes the input

    Returns: JSON with auth result info
    """
    post_data = await request.get_json()
    print('cock')
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
    if SQLModel.get_by_attrs('email', 'email', (post_data.get('email'))):
        return jsonify(info='Данный пользователь уже зарегестрирован')
    else:
        date = datetime.date.day + '/' + datetime.date.month + '/' + datetime.date.year
        SQLModel.insert((post_data.get('nickname'), post_data.get('email'), post_data.get('password'), None,
                         date, None, post_data.get('birthDate'), 'user', False))
        return jsonify(info='good')


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Unsubscribes the user from channel
    """
    post_data = request.get_json()
    Subsctiption.unsubscribe(post_data.get('from'))


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Subscribes the user to the channel
    """
    post_data = request.get_json()
    Subsctiption.subscribe(post_data.get('from'))


@app.route('/channels')
def get_channels():
    """
    Gets the channels that are in the hub selected
    Returns:
        JSON with the channels
    """
    hub = request.args.get('hub')
    users = User.get_by_attrs(cols=('nickname', 'curr_hub', 'description'), attr_cols='curr_hub', attr_values=hub, order_by='subs')
    print(jsonify(users))
    return jsonify(users)


@app.route('/channel')
def get_channel():
    """
    gets the channel info from the database and returns info about it
    Returns:
        JSON with channel info
    """
    pass



if __name__ == '__main__':
    app.run(debug=True)
