from openai import OpenAI
import os
import argparse
import sys

# Constants
CONDA_ENV_NAME = "zipbio11_AI"  # Change this to your conda environment name

def check_environment():
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

def get_gpt_response(prompt):
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    check_environment()
    parser = argparse.ArgumentParser(description='Chat with GPT from terminal')
    parser.add_argument('-p', '--prompt', help='Single prompt to send to GPT')
    parser.add_argument('text', nargs='*', help='Direct prompt text without quotes')
    args = parser.parse_args()

    if args.prompt:
        response = get_gpt_response(args.prompt)
        print(response)
    elif args.text:
        prompt = ' '.join(args.text)
        response = get_gpt_response(prompt)
        print(response)
    else:
        print("GPT Chat Interface (type 'quit' to exit)")

if __name__ == "__main__":
    main()
