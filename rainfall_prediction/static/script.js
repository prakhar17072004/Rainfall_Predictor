window.addEventListener('load', () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            document.getElementById('lat').value = position.coords.latitude;
            document.getElementById('lon').value = position.coords.longitude;
        }, (error) => {
            alert("Geolocation failed. Please allow location access or enter manually.");
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
});
