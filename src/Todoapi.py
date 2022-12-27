from flask import Flask
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/todoItems/', methods=['GET'])
@cross_origin(supports_credentials=True)
def welcome():
    return jsonify([
        {
            "name":"Buy Milk",
            "status":"Complete",
            "id":1
        },
        {
            "name":"phone bill",
            "status":"active",
            "id":2
        }
    ])
    #return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)