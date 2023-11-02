//This will access the users webcam and display the current frames
document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById('webcam');

    async function setupWebcam() {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    }

    setupWebcam();
});

