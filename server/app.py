from flask import Flask, jsonify, request
from models import SQLModel
from models.subscriptions import Subsctiption
from models.users import User
from flask_cors import CORS
import datetime
from aiohttp import web

# from aiortc import RTCPeerConnection, RTCSessionDescription
# from aiortc.contrib.media import MediaPlayer

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    """
    Gets the data from the login form and authorizes the input

    Returns: JSON with auth result info
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.get_by_attrs(('nickname', 'password'), 'email', email)
    user_pw = user[0][1]
    user_nick = user[0][0]
    if password == user_pw:
        return jsonify(result=user_nick)
    else:
        return jsonify(result='fail')


@app.route('/register', methods=['POST'])
def register():
    """
    Inserts the information about new user unto the database

    Returns:
        JSON with the result
    """
    post_data = request.get_json()
    print(post_data)
    today = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    email = post_data.get('email')
    password = post_data.get('password')
    nickname = post_data.get('nickname')
    try:
        User.insert((email, nickname, password, 'null', today, 0, 'sas', False, True, 'gaming', False))
        return jsonify(result='good')
    except:
        return jsonify(result='bad')


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
    users = User.get_by_attrs(cols=('nickname', 'curr_hub', 'description',), attr_cols=('curr_hub'), attr_values=(hub), order_by='subs DESC')
    print(jsonify(users))
    return jsonify(users)


@app.route('/channel')
def get_channel():
    """
    gets the channel info from the database and returns info about it
    Returns:
        JSON with channel info
    """
    nick = request.args.get('nickname')
    print(nick)
    stuff = User.get_by_attrs(cols=('nickname', 'subs', 'description', 'curr_hub'), attr_cols='nickname', attr_values=nick)
    print(stuff)
    return jsonify(stuff)



if __name__ == '__main__':
    app.run(debug=True)
