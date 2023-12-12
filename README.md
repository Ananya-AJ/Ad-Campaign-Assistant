# CMPE297 Term Project 
## Ad-Campaign-Assistant and chatbot

#### Members:
* Ananya Joshi
* Sanjana Kothari
* Neetha Sherra


#### Project Goals:
The objective of this project is to leverage the power of large language models, diffusion models and RAG to generate textual ads and ad banners. We create a prompt library using pinecone that has huge number of ad templates with many intricate details for many product domains, we also have a huge list of strategies, events and narratives/context to build the advertisement on. We use this RAG capability to provide an aid for the models to get more accurate and precise results and to reduce the hallucinations. Our app takes the product, event, theme as inputs and from our prompt library using Faiss fets relevant prompt which can be edited and given to the llama and stable diffusion models to generate textual ad and four image banners. We further provide a chatbot where user can interact with the model to imporve the textual ad.

#### App snapshots:

![image](https://github.com/Ananya-AJ/Ad-Campaign-Assistant/assets/111623197/93288001-9cb0-41d4-b7ac-ee759b752898)



<img width="1190" alt="image" src="https://github.com/Ananya-AJ/Ad-Campaign-Assistant/assets/111623197/a652fe14-23e7-40c5-85fb-31c31ea193c6">


![image](https://github.com/Ananya-AJ/Ad-Campaign-Assistant/assets/111623197/d037c1a8-a250-4c17-8ab8-3e7ac6763891)

#### chatgpt link of how product documents were created



#### To run the applicaton
1. Clone repo.
2. Add the documents(prompts) and json file at root level.
3. Add OpenAI api key to config.py in Code folder.
4. Install requiremnts.txt
5. To run, navigate into the Code folder and use 'python3 app.py'

#### Models
https://drive.google.com/file/d/1xTNV-QHdEwM4LW3CB4B9Vcs7oFBFlpQg/view?usp=drive_link

#### Data
https://drive.google.com/drive/folders/1j9qLL9KeW-_q8fKRDEqNttgFOhzTyVJu?usp=drive_link

#### Demo recording
https://drive.google.com/drive/folders/1EiB44XanaHX8Gn6d59sEHMw8txuE7Ot6?usp=drive_link

