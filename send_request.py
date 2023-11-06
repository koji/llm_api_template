import requests

headers = {"Content-Type": "application/json"}
user_input="Can you write a poem that describe how great life is?"

base_url = "https://6961-34-42-73-46.ngrok-free.app" # you will need to change this
endpoint = f"{base_url}/v1/completions"
response = requests.post(endpoint, headers=headers, json={
  "prompt": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n", "stop": ["\n", "###"]
},
stream=True,

)

output = response.json()
# print(output)
print(output['choices'][0]['text'])
