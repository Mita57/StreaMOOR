from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0004fd2e45b7cffc0bf4ab73db076092'

@app.route('/')
def index():
    pass


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form = form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in', form=form)


if __name__ == '__main__':
    app.run(debug=True)
