from openai import OpenAI
#OpenAI API key only works if you have Api paid key
client = OpenAI(
    api_key="# Enter your own secret key #",)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a Virtual Assistant name Jarvis skilled like Alexa and Google Cloud"},
    {"role": "user", "content": "What is programming"}
  ]
)

print(completion.choices[0].message.content)
