from flask import Flask, jsonify
from dotenv import load_dotenv
from function_jwt import write_token

load_dotenv()

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():

    print(write_token({"nombre":"Luis", "edad": 22}))

    return jsonify({"message": "Welcome to FLASK JWT API"})

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0")



