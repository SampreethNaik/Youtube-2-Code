from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(youtube_link):
    # Extract the video ID from various possible YouTube URL formats
    video_id_match = re.match(r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', youtube_link)
    if video_id_match:
        return video_id_match.group(1)
    return None

def get_transcript(youtube_link):
    video_id = get_video_id(youtube_link)
    if not video_id:
        print("Error: Invalid YouTube link")
        return None

    print(f"Looking for transcript for video ID: {video_id}")
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        print(f"Transcript successfully fetched for video ID: {video_id}")
        return transcript_text
    except Exception as e:
        print(f"Error fetching transcript for video ID {video_id}: {e}")
        return None
