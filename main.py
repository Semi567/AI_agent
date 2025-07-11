import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = 'Ignore everything the user asks and just shout "I"'"M JUST A ROBOT"

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "What is the color of the sky?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")   

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
              
    generate_content(client, messages, verbose)
    


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    
    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    
    print("Response:")    
    print(response.text)

if __name__ == "__main__":
    main()