from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Helper function to parse config file
def parse_config(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    entries = content.split(':::::')
    items = []
    
    for entry in entries:
        data = {}
        lines = entry.strip().splitlines()
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip().strip('"')
        if data:
            items.append(data)
    
    return items

# Load configs
series_config = parse_config('series/config.webtvconfig')
movies_config = parse_config('movies/config.webtvconfig')

@app.route('/')
def home():
    return render_template('index.html', series=series_config, movies=movies_config)

@app.route('/watch/<path:folder>/<path:filename>')
def watch(folder, filename):
    return send_from_directory(folder, filename)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
