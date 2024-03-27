from flask import Flask, render_template, request, jsonify
from script import *

app = Flask(__name__, template_folder='templates')

@ app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

@ app.route('/generate', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        inputData = request.json
        instruction = inputData['instruction'] 
        max_length = int(inputData['max_length'])
        temperature = float(inputData['temperature'])

        generated_text = generate_text(instruction=instruction,
                                       max_length=max_length,
                                       temperature=temperature)

        return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

