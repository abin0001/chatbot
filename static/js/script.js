const outputDiv = document.getElementById('output');
const eventSource = new EventSource('/stream');

eventSource.onmessage = function(event) {
    const responseDiv = document.createElement('div');
    responseDiv.textContent = event.data;
    outputDiv.appendChild(responseDiv);

    // Convert text to speech using SpeechSynthesis
    const msg = new SpeechSynthesisUtterance(event.data);
    window.speechSynthesis.speak(msg);
};