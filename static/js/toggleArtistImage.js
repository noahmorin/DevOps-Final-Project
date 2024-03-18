document.addEventListener('DOMContentLoaded', function() {
    const image = document.querySelectorAll('.artistImage');
    const toggleButton = document.getElementById('toggleImageButton');
  
    toggleButton.addEventListener('click', function() {
        // Swap the display of the images when button is clicked
        //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
        image.forEach(image => { 
            if (image.style.display === 'none') {
                image.style.display = 'block';
            } else {
                image.style.display = 'none';
            }
        });
    });
});
  