from flask import Flask
import datetime
buildDT = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello World!?\n'
    return '(str(currentDT))\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
