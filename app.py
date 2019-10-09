from flask import Flask, escape, request


app = Flask(__name__)

@app.route('/')
# def hello():

#     return 'Hello World!?\n'
def time_feed():
    def generate():
        yield datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
    return Response(generate(), mimetype='text') 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



# @app.route('/time_feed')
# def time_feed():
#     def generate():
#         yield datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
#     return Response(generate(), mimetype='text') 