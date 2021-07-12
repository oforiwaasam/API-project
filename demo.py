from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy


# this gets the name of the file so Flask knows it's name
app = Flask(__name__)
app.config['SECRET_KEY'] = '2e0d61f47091d568b375cd9f2838e9db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


# this tells you the URL the method below is related to
@app.route("/")
@app.route("/home")
def home():
    # this prints HTML to the webpage
    return render_template('home.html', subtitle='Home Page',
                           text='Welcome to the Tower of Hanoi game!')


@app.route("/game")
def game():
    return render_template('game.html', subtitle='Game Page',
                           text='This is the game page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # if so - send to home page
    return render_template('register.html', title='Register', form=form)


# this should always be at the end
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
