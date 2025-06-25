import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions
from prompts import system_prompt

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
    verbose = is_verbose()
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config,
    )
    
    if (verbose):
        token_count = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {token_count}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
        return response.text
    
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if __name__ == "__main__":
    main()
