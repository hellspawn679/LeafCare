import requests
import json

# Define the data you want to send in the POST request
data = {'image': 'https://cals.cornell.edu/sites/default/files/styles/three_card_callout/public/2021-02/commrust4-9-250x376.gif?h=2aff6ec4&itok=Vrb_zo9i'}  # Replace this with your actual data

# Convert the data to JSON format
json_data = json.dumps(data)

# Make the POST request to your Flask API endpoint
response = requests.post('http://127.0.0.1:5000/', json=json_data)

# Print the response from the server
print(response.json())
