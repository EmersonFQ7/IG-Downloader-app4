from flask import Flask, request, jsonify, render_template, send_from_directory
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

# Crear carpeta si no existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-ig', methods=['POST'])
def download_instagram():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "Falta la URL"}), 400

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({"message": "Descarga exitosa"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list-videos')
def list_videos():
    files = os.listdir(DOWNLOAD_FOLDER)
    # Solo mostrar archivos de video
    videos = [f for f in files if f.endswith(('.mp4', '.mkv', '.webm'))]
    return jsonify(videos)

@app.route('/videos/<filename>')
def serve_video(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)