## COCOCHAT
This is a slack chat bot that uses publicly available LLM endpoints from openai.org and anyscale.com. This chat bot is designed to support multi-user chat threads primarily for collaborative content production. Currently this is in active development and not all of the features are implemented. The live instance of the app is hosted through Azure App Service as a Web App (powered by Flask). 

Azure endpoint for the service: http://cocochat-test.azurewebsites.net/

### Developer Info:
- name: Soumit Salman Rahman (personal)
- github: https://github.com/soumitsalman/
- email: soumitsr@gmail.com
- linkedIn: https://www.linkedin.com/in/soumitsrahman/

### Features:
- [x] By changing the deployment's environment variables it can be run through any of the following LLMs: 
    - mistralai/Mixtral-8x7B-Instruct-v0.1
    - mistralai/Mistral-7B-Instruct-v0.1
    - HuggingFaceH4/zephyr-7b-beta
    - codellama/CodeLlama-34b-Instruct-hf
    - meta-llama/Llama-2-13b-chat-hf
    - gpt-4-1106-preview
    - gpt-3.5-turbo-1106
- [x] In direct message mode the chat bot will respond to every user message
- [x] In channel/group conversation it will ONLY respond if the message mentions the app/bot
- [x] Slack input message markdown santization/normalization
- [ ] Reading conversation history if it joins the channel later
- [ ] Ability to switch underlying LLM without loosing the chat context
- [ ] Ability to switch the LLM instructions during runtime by a user
- [ ] Internet search ability

### Dependencies:
Uses https://github.com/soumitsalman/openai-utilities (pip install openai-utilities) SDK as the wrapper on top of openai SDK.

### Contribution Guideline:
Feel free to make contributions to the code as you see fit. There is currently no test automation or github workflow set up. So #YOLO. If you want more wrapped capabilities feel free to reach out.


