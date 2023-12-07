//This will access the users webcam and display the current frames
document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById('webcam');

    async function setupWebcam() {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    }

    setupWebcam();
});

 // Function to clear the jumbotron text
document.addEventListener('DOMContentLoaded', function () {
    function clearJumbotron() {
        var jumbotron = document.getElementById('transcriptionJumbotron');

        jumbotron.innerHTML = '';
    }

    var clearButton = document.getElementById('ClearButton');
    clearButton.addEventListener('click', clearJumbotron);
});

// Function to read text using text-to-speech
document.addEventListener('DOMContentLoaded', function () {
    function readTextAloud() {

        var jumbotronText = document.getElementById('transcriptionJumbotron').innerText;

        var synth = window.speechSynthesis;
        var utterance = new SpeechSynthesisUtterance(jumbotronText);

        synth.speak(utterance);
    }

    var dictateButton = document.getElementById('DictateButton');
    dictateButton.addEventListener('click', readTextAloud);
});

// Get the webcam video element and Record button
document.addEventListener('DOMContentLoaded', function () {
    
    var webcam = document.getElementById('webcam');
    var recordButton = document.getElementById('RecordButton');

    var mediaRecorder;
    var recordedChunks = [];

    function toggleRecording() {
        if (!mediaRecorder || mediaRecorder.state === 'inactive') {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function (stream) {
                    webcam.srcObject = stream;
                    mediaRecorder = new MediaRecorder(stream);

                    mediaRecorder.ondataavailable = function (event) {
                        if (event.data.size > 0) {
                            recordedChunks.push(event.data);
                        }
                    };

                    mediaRecorder.onstop = function () {
                        var blob = new Blob(recordedChunks, { type: 'video/webm' });
                        var url = URL.createObjectURL(blob);

                        webcam.src = url;
                        recordedChunks = [];
                    };

                    mediaRecorder.start();
                    recordButton.textContent = 'Stop Recording';
                })
                .catch(function (error) {
                    console.error('Error accessing webcam:', error);
                });
        } else if (mediaRecorder.state === 'recording') {

            mediaRecorder.stop();
            recordButton.textContent = 'Record';
        }
    }
    
    recordButton.addEventListener('click', toggleRecording);
});

/*Backend to jumbrotron */
var sendToSean = `${predicted_class_encoded[0].capitalize()}${questionMark}`;

// Update the content of the jumbotron
document.getElementById('transcriptionJumbotron').getElementsByTagName('p')[0].innerText = sendToSean;

