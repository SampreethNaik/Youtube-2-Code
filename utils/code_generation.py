import openai

# Configure your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_code(transcript, language):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": f"Generate code in {language}."},
            {"role": "user", "content": transcript}
        ],
        functions=[
            {
                "name": "generate_code",
                "description": "Generates code based on a transcript.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transcript": {"type": "string"},
                        "language": {"type": "string"}
                    },
                    "required": ["transcript", "language"]
                }
            }
        ],
        function_call="auto"
    )
    code = response['choices'][0]['message']['content']
    return code
