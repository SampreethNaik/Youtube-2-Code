import google.generativeai as genai

# Configure your Gemini API key here
genai.api_key = 'YOUR_GEMINI_API_KEY'

def generate_code(transcript, language):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate code in {language} based on this transcript:\n{transcript}"
    response = model.generate_content(prompt)
    code = response.text
    return code
