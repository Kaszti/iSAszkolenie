from flask import Flask
app = Flask(__name__)
@app.route('/')
def witaj():
    return 'Hello'
app.debug = True
app.run()