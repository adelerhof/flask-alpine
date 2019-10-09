from flask import Flask, escape, request


app = Flask(__name__)

@app.route('/')
def hello():

    # return 'Hello World!?\n'
    return '"And Shepherds we shall be\nFor thee, my Lord, for thee.\nPower hath descended forth from Thy hand\nOur feet may swiftly carry out Thy commands.\nSo we shall flow a river forth to Thee\nAnd teeming with souls shall it ever be.\nIn Nomeni Patri Et Fili Spiritus Sancti."\n\n\n\n https://www.youtube.com/watch?v=TBLgTBpW4zs \n\n\n    '
# def time_feed():
#     def generate():
#         yield datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
#     return Response(generate(), mimetype='text') 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



# @app.route('/time_feed')
# def time_feed():
#     def generate():
#         yield datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
#     return Response(generate(), mimetype='text') 