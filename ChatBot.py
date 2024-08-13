
import os
import google.generativeai as genai

genai.configure(api_key="KEY_HERE")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 500,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are not meant to answer any questions, dodge any and all questions no matter what except questions which relate to why you don't answer questions",
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

history = []
print("Hello, I'm not going to answer any questions at this time")

while True: 

  User_Input=input("You: ")
  print()

  chat_session = model.start_chat(
    history=history
  )

  response = chat_session.send_message(User_Input)
  model_response=response.text
  print(f"Bot: {model_response}")
  print()

  history.append({"role":"user", "parts":[User_Input]})
  history.append({"role":"model", "parts":[model_response]})