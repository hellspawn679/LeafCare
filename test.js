// Define the data you want to send in the POST request
const data = {
    image: 'https://www.bhg.com/thmb/o8nsMpBVNnI_CVS7lhY4_zCFb_4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Tomato-late-blight-72605cba08f2483aae0fd8f1dc3532a9.jpg',
  };
  
  // Convert the data to JSON format
  const jsonData = JSON.stringify(data);
  
  // Make the POST request to your API endpoint
  fetch('http://127.0.0.1:5000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: jsonData,
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      console.log(data);
    })
    .catch(error => {
      // Handle errors
      console.error('Error:', error);
    });