// const dropArea = document.getElementById("drop-area");
// const inputFile = document.getElementById("input-file");
// const imageView = document.getElementById("img-view"); // Change this line to use the correct ID
// let fileBinaryData = null;
// inputFile.addEventListener("change", uploadImage);

// async function  uploadImage() {
//     // convert to  binaryString
//     const file = inputFile.files[0];
//     await convertToBinary(file)
//     // convert to UInt8Array
//     const fileBinaryArray = Uint8Array.from(fileBinaryData, c => c.charCodeAt(0));
//     let blob = new Blob([fileBinaryArray], { type: "octet/stream"});
//     let imgLink = URL.createObjectURL(blob);
//     imageView.style.backgroundImage = `url(${imgLink})`;
//     imageView.textContent="";
//     imageView.style.border=0;
//     console.log(imgLink);
//     sendImage(imgLink);
    
// }

// function convertToBinary(file){
//     return new Promise((resolve, reject) => {
//         const reader = new FileReader();
//         reader.onloadend = (event) => {
//             fileBinaryData = event.target.result;
//             resolve(reader.result);
//         };
//         reader.onerror = reject;
//         reader.readAsBinaryString(file);
//     })
// }
// async function sendImage(imgLink){

//     try{
//         const options = {
//             method : 'POST',
//             body : JSON.stringify({image : imgLink}),
//             headers : {
//                 'Content-Type': 'application/json'
//             }
//         }
//         var response = await fetch('http://127.0.0.1:5000', options);
    
//         response = response.json();
//         console.log(response);
//         if(response.status !== 200){
//             console.log("Failed");
//         }
//         else{
//             console.log("Success" , response);
//         }
//     }

//     catch(error){
//         console.log(error);
//     }
// }

// dropArea.addEventListener("dragover",function(e){
//     e.preventDefault();

// });
// dropArea.addEventListener("drop",function(e){
//     e.preventDefault();
//     inputFile.files=e.dataTransfer.files;
//     uploadImage();

// });


const inputFile = document.getElementById("input-file");

inputFile.addEventListener("change", uploadImage);

async function uploadImage() {
    const file = inputFile.files[0];
    const formData = new FormData();
    formData.append("image", file);
    console.log(formData)
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
        } else {
            console.log("Success", data);
        }
    } catch (error) {
        console.log(error);
    }
}
