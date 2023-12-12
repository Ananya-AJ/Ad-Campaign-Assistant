# CMPE297 Term Project 
## Ad-Campaign-Assistant and chatbot

#### Members:
* Ananya Joshi
* Sanjana Kothari
* Neetha Sherra


#### Project Goals:
The objective of this project is to leverage the power of large language models, diffusion models and RAG to generate textual ads and ad banners. We create a prompt library using pinecone that has huge number of ad templates with many intricate details for many product domains, we also have a huge list of strategies, events and narratives/context to build the advertisement on. We use this RAG capability to provide an aid for the models to get more accurate and precise results and to reduce the hallucinations. Our app takes the product, event, theme as inputs and from our prompt library using Faiss fets relevant prompt which can be edited and given to the llama and stable diffusion models to generate textual ad and four image banners. We further provide a chatbot where user can interact with the model to imporve the textual ad.

#### App snapshots:


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

