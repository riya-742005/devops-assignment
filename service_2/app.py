from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"service": "service2"})  # change to service2 in service_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # change port to 5002 in service_2
