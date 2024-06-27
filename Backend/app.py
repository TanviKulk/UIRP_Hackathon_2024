from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests from your React frontend


@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Here you would analyze the file and determine if it's a weed,
        # what type of weed it is, and how to eradicate it.
        # This is just a placeholder implementation.
        analysis_result = {
            'is_weed': True,
            'weed_species': 'Dandelion',
            'eradication_methods': 'Apply herbicide or manually remove it.'
        }
        return jsonify(analysis_result)


if __name__ == '__main__':
    app.run(debug=True)
