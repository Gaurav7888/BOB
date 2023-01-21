import os
print(os.environ())
secret = {{secret.GIT_TOKEN }}
print(secret)
import openai



openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
