from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import yt_dlp
import os
import glob

app = Flask(__name__)
CORS(app)

DOWNLOADS_FOLDER = "downloads"
os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)  # Ensure folder exists

@app.route('/')
def index():
    return "Welcome to the YouTube Video Downloader API!"

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    video_url = data.get('video_url')
    desired_resolution = data.get('resolution', 'best')

    if not video_url:
        return jsonify({"error": "Video URL is required"}), 400

    try:
        # Download options
        ydl_opts = {
            'outtmpl': f'{DOWNLOADS_FOLDER}/%(title)s.%(ext)s',
            'format': f'bestvideo[height<={desired_resolution}]+bestaudio/best',
            'merge_output_format': 'mp4',
          # Pass the cookies file if needed
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            filename = filename.replace('.webm', '.mp4')  # Ensure MP4 format

        # Find the latest downloaded file
        downloaded_files = glob.glob(f"{DOWNLOADS_FOLDER}/*.mp4")
        if not downloaded_files:
            return jsonify({"error": "File not found"}), 404
        
        latest_file = max(downloaded_files, key=os.path.getctime)  # Get the latest file

        return send_file(latest_file, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)