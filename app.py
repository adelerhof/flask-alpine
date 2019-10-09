from flask import Flask, escape, request
import datetime
buildDT = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def hello():

    # return 'Hello World!?\n'
    # name = request.args.get("name", "World")
    return f'(str(currentDT))\n'

    # return f'Hello, {escape(name)}!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
