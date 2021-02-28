from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello World!'

@app.route('/home')
def Home():
    return '<div> <h1>Deep Learning Model</h1><br/><h2>Cat vs Dog</h2> </div>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hi! %s</h2>" % username    


if __name__ == "__main__":
    app.run()