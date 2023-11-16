import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import requests 

from io import BytesIO

# Define the path to your image
#image_path = '/508-icon.508-icon.png'

# 1. Preprocess the input image
# Define a transformation for image preprocessing
preprocess = AutoFeatureExtractor.from_pretrained("yusuf802/Leaf-Disease-Predictor")

# Load and preprocess the image
#image = Image.open(image_path)
img =requests.get("https://extension.umd.edu/sites/extension.umd.edu/files/styles/optimized/public/2021-05/hgic_veg_septoria%20leaf%20spot1_1600.jpg?itok=WY6ErcxV")

image=Image.open(BytesIO(img.content))
inputs = preprocess(images=image, return_tensors="pt")

# 2. Load the pre-trained feature extractor and model
model = AutoModelForImageClassification.from_pretrained("yusuf802/Leaf-Disease-Predictor")
model.eval()

# 3. Pass the preprocessed image through the feature extractor and the model
with torch.no_grad():
    outputs = model(**inputs)

# 4. Obtain the predictions
logits = outputs.logits
probabilities = torch.softmax(logits, dim=1)

# Assuming you want to get the top predicted class and its probability
predicted_class = torch.argmax(probabilities, dim=1).item()
predicted_probability = probabilities[0][predicted_class].item()

# Print the results
print(f"Predicted Class: {predicted_class}")
print(f"Predicted Probability: {predicted_probability}")


import json
json_data='''{"0": "Apple_Black_rot",
    "1": "Apple_Cedar_apple_rust",
    "10": "Corn_(maize)_healthy",
    "11": "Cotton_leaf_diseased",
    "12": "Cotton_leaf_fresh",
    "13": "Grape_Black_rot",
    "14": "Grape___Esca_(Black_Measles)",
    "15": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "16": "Grape___healthy",
    "17": "Orange_Haunglongbing_(Citrus_greening)",
    "18": "Orange__Black_Rot",
    "19": "Orange__Canker",
    "2": "Apple_Powdery_mildew",
    "20": "Orange__Healthy",
    "21": "Peach_Bacterial_spot",
    "22": "Peach_healthy",
    "23": "Pepper,_bell_Bacterial_spot",
    "24": "Pepper,_bell_healthy",
    "25": "Potato_Early_blight",
    "26": "Potato_Late_blight",
    "27": "Potato_healthy",
    "28": "Squash_Powdery_mildew",
    "29": "Strawberry_Leaf_scorch",
    "3": "Apple_healthy",
    "30": "Strawberry_healthy",
    "31": "Tomato_Bacterial_spot",
    "32": "Tomato_Early_blight",
    "33": "Tomato_Late_blight",
    "34": "Tomato_Leaf_Mold",
    "35": "Tomato_Septoria_leaf_spot",
    "36": "Tomato_Spider_mites_Two_spotted_spider_mite",
    "37": "Tomato_Target_Spot",
    "38": "Tomato_Tomato_Yellow_Leaf_Curl_Virus",
    "39": "Tomato_Tomato_mosaic_virus",
    "4": "Apple_scab",
    "40": "Tomato_healthy",
    "41": "Wheat_healthy",
    "42": "Wheat_leaf_rust",
    "43": "Wheat_nitrogen_deficiency",
    "5": "Cherry_(including_sour)_Powdery_mildew",
    "6": "Cherry_(including_sour)_healthy",
    "7": "Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot",
    "8": "Corn_(maize)_Common_rust",
    "9": "Corn_(maize)_Northern_Leaf_Blight"}'''
student_details =json.loads(json_data)


print(student_details[str(predicted_class)])