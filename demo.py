from flask import Flask, render_template, url_for

app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name

#@app.route("/")                          # this tells you the URL the method below is related to
@app.route("/home")
def home():
    return render_template('home.html', subtitle = 'Home Page', text = 'Welcome to the Tower of Hanoi game!')        # this prints HTML to the webpage

@app.route("/game")
def game():
    return render_template('game.html', subtitle='Game Page', text='This is the game page')
  
  
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")