from flask import Flask, request, jsonify
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import os

app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image_file = request.files['image']
    if image_file:
        image_path = os.path.join('image', image_file.filename)
        image_file.save(image_path)

        # Preprocess the uploaded image
        preprocess = AutoFeatureExtractor.from_pretrained("yusuf802/Leaf-Disease-Predictor")
        image = Image.open(image_path)
        inputs = preprocess(images=image, return_tensors="pt")

        # Load the pre-trained model
        model = AutoModelForImageClassification.from_pretrained("yusuf802/Leaf-Disease-Predictor")
        model.eval()

        # Pass the preprocessed image through the model
        with torch.no_grad():
            outputs = model(**inputs)

        # Obtain the predictions
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)

        # Assuming you want to get the top predicted class and its probability
        predicted_class = torch.argmax(probabilities, dim=1).item()
        predicted_probability = probabilities[0][predicted_class].item()

        # Return the results
        return jsonify({
            'message': 'Image uploaded and processed successfully',
            'image_path': image_path,
            'predicted_class': predicted_class,
            'predicted_probability': predicted_probability
        }), 200
    else:
        print('1')
        return jsonify({'error': 'No image provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
