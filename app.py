from flask import Flask, request, jsonify, render_template
from utils.youtube_transcript import get_transcript

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code', methods=['POST'])
def generate_code_endpoint():
    data = request.json
    youtube_link = data.get('youtube_link')
    
    if not youtube_link:
        app.logger.error('Invalid input: No YouTube link provided')
        return jsonify({'error': 'Invalid input'}), 400
    
    app.logger.debug(f"Fetching transcript for: {youtube_link}")
    transcript = get_transcript(youtube_link)
    if not transcript:
        app.logger.error(f'Failed to extract transcript for: {youtube_link}')
        return jsonify({'error': 'Failed to extract transcript'}), 500
    
    app.logger.debug(f'Transcript fetched successfully for: {youtube_link}')
    return jsonify({'transcript': transcript})

if __name__ == '__main__':
    app.run(debug=True)
