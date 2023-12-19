const inputFile = document.getElementById("input-file");

inputFile.addEventListener("change", uploadImage);

async function uploadImage() {
    const file = inputFile.files[0];
    const formData = new FormData();
    formData.append("image", file);
    console.log(formData);
    await sendImage(formData);
}

async function sendImage(formData) {
    try {
        const options = {
            method: 'POST',
            body: formData,
        };

        const response = await fetch('http://127.0.0.1:5000', options);
        const data = await response.json();

        if (response.status !== 200) {
            console.log("Failed");
            alert("Failed to upload image. Please try again.");
        } else {
            console.log("Success", data);
            alert("Image uploaded successfully. Response data: " + JSON.stringify(data));
            document.querySelector('.audio_cont').innerHTML+=`<audio class="hui" src="welcome.mp3" autoplay ></audio>`
            console.log(document.querySelector('.audio_cont').innerHTML)
        }
    } catch (error) {
        console.log(error);
        alert("An error occurred while uploading the image. Please try again.");
    }
}