import openai
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

openai.api_key = OPENAI_API_KEY

def generate_text(prompt, max_tokens=50, temperature=0.7, n=1):
    """
    Generate text using OpenAI's GPT model.

    :param prompt: The text prompt to be completed by the model.
    :param max_tokens: The maximum number of tokens to generate in the response.
    :param temperature: Controls the creativity of the model's output. Higher values result in more random outputs.
    :param n: The number of independent completions to generate for the prompt.
    :return: A list of generated text completions.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature,
    )

    return [choice.text.strip() for choice in response.choices]

def generate_commit_message(git_diff):
    """
    Generate a commit message based on the given Git diff.

    :param git_diff: A string representing the Git diff.
    :return: A generated commit message.
    """
    prompt = f"Based on the following Git diff, generate a commit message:\n\n{git_diff}\n\nCommit message:"
    commit_messages = generate_text(prompt, max_tokens=30, temperature=0.5, n=1)
    return commit_messages[0]
