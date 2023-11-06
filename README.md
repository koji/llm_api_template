# LLM API Template

## What is this?
This is a jupyter notebook that uses LLMs via endpoints. This is using [llama.cpp](https://github.com/ggerganov/llama.cpp), [ngrok](https://ngrok.com/), and a model from [TheBloke](https://huggingface.co/TheBloke)
The base jupyter notebook uses [zephyr-7b](https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF).

## How to use
[Requiremetns]  
- Google account for Google colab https://colab.google/
- ngrok account https://ngrok.com

#### step0. create the above accounts  
#### step1. Copy the jupyter notebook
#### step2. Create a secreat key
There is the key icon in Google colab's sidebar. You will need to add your token as a secret key. In the jupyter notebook, I named `NGROK`. You can change that into anything you want.    
#### step3. Run the jupyter notebook
After setting a new secreat key, you can run the jupyter notebook to run the API server.
#### step4. Check the API server
If everything works properly, you can acces https://ngrok_address/docs and you will see something like 👇  
You can see the all available endpoints. 
![Screenshot 2023-11-05 193747](https://github.com/koji/llm_api_template/assets/474225/561830f6-f3a7-4c71-bc39-c857c8eb7ad9)

#### step5. Call the endpoint
Now you can call the endpoint via any language you like. In this repo, I put a python code as a sample.  
What you need to do is to change the url.  

![Screenshot 2023-11-05 171110](https://github.com/koji/llm_api_template/assets/474225/240bd549-60c9-4332-8b69-f54802c60b7b)


## How to use a different model?
If you want to use a different model such as llama2-7b, mistral-7b, etc, you will need to download the model from  https://huggingface.co/TheBloke and modify the jupyter notebook a little bit.

```py
from llama_cpp import Llama
llm = Llama(model_path="zephyr-7b-alpha.Q5_K_M.gguf") # 👈 you will need to change this model path.
output = llm("Q: can you write a python script for fizz buzz? A: ", max_tokens=2048, stop=["Q:", "\n"], echo=True)
print(output)
```
