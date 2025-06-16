import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def print_help_message():
    print("ERROR: NO PROMPT WAS PROVIDED")
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here"')
    print('Example: python main.py "How do I build a calculator app?"')

def load_user_prompt():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print_help_message()
        sys.exit(1)
    return " ".join(args)

def is_verbose():
    return "--verbose" in sys.argv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = load_user_prompt()
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    
    if (is_verbose()):
        token_count = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {token_count}")
        print(f"Response tokens: {response_tokens}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
