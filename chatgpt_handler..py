import openai


openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )

    return response['choices'][0]['text']
