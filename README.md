# Plotly Dash Chatbot Template

## Newsletter
👉🏽 Do you enjoy our content and want to read super-detailed articles about AI? If so, subscribe to our [Tinz Twins Hub](https://tinztwinshub.com/blog/) and get our popular data science cheat sheets for FREE.

## General
This project contains a well structured Chatbot App with Plotly Dash and LangChain. Feel free to use this example as the basis for your next web-based Chatbot App.

## Local Development
* Create and activate a virtual environment (e.g. [conda](https://docs.conda.io/en/latest/)): 
    * `conda create -n ai-chatbot python=3.9.12`
    * `conda activate ai-chatbot`
* Please install the dependencies with the following command: `pip install -r requirements.txt`
* Please create a new environment file `.env_dev` in the chatbot/environment folder. The file `.env_dev_template` serves as a template. Add your OpenAI API key.
* Navigate to the chatbot folder. Execute the following command: `python index.py`
* Open the app at http://127.0.0.1:7000

## Dockerize the Chatbot App (Production Environment)
* Please create a new environment file `.env` in the chatbot/environment folder. The file `.env_template` serves as a template. Add your OpenAI API key.
* Build the app with the following command: `docker build -t chatbot-app:latest .`
* Run the app with the following command: `docker run --name chatbot -d -p 7000:7000 chatbot-app`
* Open the app at http://0.0.0.0:7000.

## Detailed tutorial
* [Tutorial](/tutorial/)

## Support this project
👉🏽 [Support our work](https://digitalproducts.tinztwinshub.com/l/chatbot-template)

## Follow us for more content
* [X](https://x.com/tinztwins)
* [Tinz Twins Hub](https://tinztwinshub.com)

⭐️ Star the repo if you find it useful!
