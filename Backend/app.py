from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
# Path to Infer.py
script_path = '/Users/srivanthdoddala/Desktop/UIRP_Hackathon_2024/Infer.py'

# Add the directory containing your script to sys.path if needed
sys.path.append('/Users/srivanthdoddala/Desktop/UIRP_Hackathon_2024')

# Import functions from Infer.py
import importlib.util
spec = importlib.util.spec_from_file_location("Infer", script_path)
infer_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(infer_module)

# Access the functions
predicts = infer_module.predicts

# Initialize Flask app
app = Flask(__name__)

# Management strategies dictionary (example)
management_strategies = {
    "Crabgrass": {
        "Biological Control": "Introduce natural enemies like fungal pathogens (e.g., Drechslera spp.) that specifically target crabgrass.",
        "Cultural Control": "Maintain a dense and healthy lawn through proper fertilization and mowing. Use crop rotation with crops that create dense canopies to shade out crabgrass.",
        "Mechanical Control": "Regularly hand-pull or hoe young crabgrass plants before they set seed. Use mulch to prevent crabgrass seeds from germinating.",
        "Chemical Control": "Apply pre-emergent herbicides, such as dithiopyr or pendimethalin, in early spring to prevent crabgrass seed germination. Post-emergent herbicides like quinclorac can be used on actively growing crabgrass."
    },
    "Palmer Amaranth": {
        "Biological Control": "Utilize cover crops like cereal rye or hairy vetch to suppress Palmer amaranth by outcompeting it for resources.",
        "Cultural Control": "Rotate crops with different growth habits and planting dates to disrupt Palmer amaranth's lifecycle. Use competitive crops like soybeans with narrow row spacing to shade out Palmer amaranth.",
        "Mechanical Control": "Implement timely tillage to destroy seedlings before they establish. Use inter-row cultivation in row crops to physically remove Palmer amaranth plants.",
        "Chemical Control": "Employ a combination of pre-emergent and post-emergent herbicides with different modes of action to reduce resistance development. Examples include metolachlor (pre-emergent) and dicamba (post-emergent)."
    },
    "Ragweed": {
        "Biological Control": "Encourage natural predators, such as ragweed beetles (Ophraella communa), to feed on ragweed.",
        "Cultural Control": "Implement crop rotation with competitive crops like small grains that establish quickly and shade out ragweed. Use cover crops such as clover to suppress ragweed germination.",
        "Mechanical Control": "Regularly mow or till ragweed plants before they flower and set seed. Use flame weeding for young ragweed plants in early growth stages.",
        "Chemical Control": "Apply pre-emergent herbicides like isoxaben to prevent ragweed seed germination. Post-emergent options include glyphosate for spot treatments in non-crop areas."
    },
    "Waterhemp": {
        "Biological Control": "Research is ongoing, but fungal pathogens such as Phomopsis amaranthicola have shown potential in targeting waterhemp.",
        "Cultural Control": "Practice crop rotation with crops that have different planting dates and growth habits to break waterhemp's lifecycle. Use cover crops like winter wheat to outcompete waterhemp.",
        "Mechanical Control": "Implement timely and frequent cultivation to control waterhemp seedlings. Employ no-till practices to reduce soil disturbance and minimize waterhemp seed germination.",
        "Chemical Control": "Use a diversified herbicide program, including pre-emergent herbicides like metribuzin and post-emergent herbicides like fomesafen. Rotate herbicides with different modes of action to prevent resistance."
    }
}

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Predict the weed name
        WeedName = predicts(file.filename)

        # Retrieve management strategies based on WeedName
        eradication_methods = management_strategies.get(WeedName, {})

        # Prepare analysis result JSON
        analysis_result = {
            'is_weed': True if WeedName else False,
            'weed_species': WeedName,
            'eradication_methods': eradication_methods
        }

        return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
