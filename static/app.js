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
button.addEventListener('click', () => {
  const context = photo.getContext('2d');
  context.drawImage(video, 0, 0, photo.width, photo.height);

  const imageData = photo.toDataURL('image/jpeg');
  console.log('Image data:', imageData); // For debugging

  // Send image data to Python API (replace with your API endpoint and logic)
  // fetch('/your-api-endpoint', {
  //   method: 'POST',
  //   body: JSON.stringify({ imageData })
  // })
  // .then(response => response.json())
  // .then(data => {
  //   prediction.textContent = `Predicted object: ${data.class}`;
  // })
  // .catch(err => console.error(err));

  // Placeholder: Display a message while waiting for API response
  prediction.textContent = 'Processing image...';
});

