import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')

# Arguments
args = sys.argv

# Check if prompt is provided or not
if not args[1]:
    raise TypeError('No prompt provided.')
    sys.exit(1)

else:

    # Store messages
    user_prompt = args[1]
    #verbose = args[2]

    messages = [
        types.Content(role='user', parts=[types.Part(text=user_prompt)]),
    ]

    # Gemini client creation and generate content
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )

    metadata = response.usage_metadata
    prompt_tokens = metadata.prompt_token_count
    response_tokens = metadata.candidates_token_count

    # If yes --verbose 
    if '--verbose' in args:
        print('User prompt:', response.text)
        print('Prompt tokens:', prompt_tokens)
        print('Response tokens:', response_tokens)
    else:
        # If no --verbose    
        print(response.text)

    sys.exit(0)