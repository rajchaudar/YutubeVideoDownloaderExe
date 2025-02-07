document.getElementById('download-btn').addEventListener('click', function () {
    const videoUrl = document.getElementById('video-url').value;
    const resolution = document.getElementById('resolution').value || 'best';

    if (!videoUrl) {
        alert("Please enter a valid YouTube video URL.");
        return;
    }

    fetch('http://127.0.0.1:5000/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ video_url: videoUrl, resolution: resolution })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.error); });
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'video.mp4';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => {
        alert(`Error: ${error.message}`);
    });
});