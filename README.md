# YouTube Video Downloader

This tool is a YouTube video downloader API built using Flask and a web extension with a simple interface to download videos in various resolutions.

## Features

- 🎥 Download videos in multiple resolutions (360p, 480p, 720p, 1080p, 1440p, 2160p)
- 🖱️ Simple interface for users to enter the URL and choose a resolution
- 🔗 Flask API for backend processing and video downloading
- 🧩 Web extension for easy access to downloading

## Technologies Used

- 🐍 Flask (Python backend)
- 🎬 yt-dlp (video downloading)
- 🌍 Flask-CORS (Handling cross-origin issues)
- 🌐 Web technologies (HTML, CSS, JS)
- 🖥️ Manifest v3 (browser extension)

## Installation & Setup

### Backend (Flask API)

1. 📂 Clone the repository:
   ```bash
     https://github.com/rajchaudar/YutubeVideoDownloaderExe.git
     cd YutubeVideoDownloaderExe
   ```
2. 📦 Install dependencies:
   ```bash
   pip install flask flask-cors yt-dlp
   ```
3. ▶️ Run the Flask API:
   ```bash
   python application.py
   ```
   The API will start on `http://127.0.0.1:5000/`

### Browser Extension

1. 🔧 Open `chrome://extensions/` in the browser.
2. 🏗️ Enable "Developer Mode" (toggle in the top-right corner).
3. 📤 Click "Load Unpacked" and select the extension folder.
4. 🎉 The extension should now be available in the browser.

## API Endpoints

### `GET /`

- 💬 Returns a welcome message.

### `POST /download`

- **Request:**
  ```json
  {
    "video_url": "https://www.youtube.com/watch?v=example",
    "resolution": "1080"
  }
  ```
- **Response:**
  - ✅ If successful, it returns the downloaded video.
  - ❌ If unsuccessful, it returns an error message.

## Usage

1. 🔍 Open the browser extension.
2. 🔗 Enter the video URL.
3. 🎚️ Select the resolution.
4. ⬇️ Click the "Download" button.
5. 📥 The video will be downloaded automatically.

## Notes

- ⚙️ Ensure `yt-dlp` is installed and up to date.
- 🚫 Some videos may have restrictions that prevent downloading.
- 🔄 The API must be running for the browser extension to work.

## License

This project is open-source and available under the MIT License.

### MIT License

© [2025] [Shivraj Chaudar]

Permission is granted, free of charge, to any person obtaining a copy of this software to use, modify, distribute, and build upon the software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

