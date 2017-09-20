from flask import Flask, jsonify, render_template, request
import json
app = Flask(__name__)



@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)

    j= jsonify(result=a+b)
    print 'j',j
    return j

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()