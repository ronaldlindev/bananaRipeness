const video = document.getElementById('video');
const photo = document.getElementById('photo');
const button = document.getElementById('capture');
const prediction = document.getElementById('prediction');

// Original code from https://kmtabish.medium.com/access-devices-camera-from-static-html-page-using-javascript-camera-api-7b0117f4e2db
var ctx;
if(navigator && navigator.mediaDevices){
    const options = { audio: false, video: { facingMode: "user", width: 300, height: 300  } }
    navigator.mediaDevices.getUserMedia(options)
    .then(function(stream) {
        video = document.querySelector('video');
        video.srcObject = stream;
        video.onloadedmetadata = function(e) {
          video.play();
        };
        ctx = photo.getContext('2d');
    })
    .catch(function(err) {
        console.log('err');
    });

} else {
    console.log("camera API is not supported by your browser")
}


// When Capture Clicked
button.addEventListener('click', async () => {
  prediction.textContent = 'Processing image...';
  try {
    ctx = photo.getContext('2d');
    ctx.drawImage(video, 0, 0, photo.width, photo.height);
  
    const photoData = photo.toDataURL('image/jpeg');
    console.log('Image data:', photoData); 

    const response = await fetch('/predict', {
      method: 'POST',
      body: JSON.stringify({imageData: photoData})
    });
    if (response.ok) {
      const data = await response.json();
      let ripeness = translateRipeness(data.class);
      console.log(data.class)
      prediction.textContent = 'Predicted Ripeness: ' + ripeness;
    } else {
      throw new Error('API call failed: ${response.status}');
    }
  } catch (error) {
    prediction.textContent = 'Image error: please try again'
  }

  function translateRipeness(val) {
    switch(val) {
      case 0:
        return "Unripe";
      case 1:
        return "Ripe";
      case 2:
        return "Overripe";
      case 3: 
        return "Rotten";
    }
  }

});

