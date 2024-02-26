const video = document.getElementById('video');
const photo = document.getElementById('photo');
const button = document.getElementById('capture');
const prediction = document.getElementById('prediction');

// Request Camera access
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => console.error(err));

// When Capture Clicked
button.addEventListener('click', async () => {
  prediction.textContent = 'Processing image...';
  try {
    const context = photo.getContext('2d');
    context.drawImage(video, 0, 0, photo.width, photo.height);
  
    const photoData = photo.toDataURL('image/jpeg');
    console.log('Image data:', photoData); // For debugging
  
  
    const response = await fetch('/predict', {
      method: 'POST',
      body: JSON.stringify({imageData: photoData})
    });
    if (response.ok) {
      const data = await response.json();
      console.log("nice")
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

