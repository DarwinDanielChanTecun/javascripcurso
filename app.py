from flask import Flask, jsonify
import xml.etree.ElementTree as ET


app = Flask(__name__)
datos = []

@app.route('/')
def index():
    return jsonify({"message": "Hello World!"})

@app.route('/ejemplo')
def saludo():
    return jsonify({"message": "todo esta funcionando correctamente"})



if __name__ == '__main__':
    app.run(debug=True, port=5000)