# Simple-GPT-4-API-Query

This is a simple Python script that demonstrates how to use the GPT-4 API in a Jupyter Notebook environment. It allows users to input prompts and receive responses from the GPT-4 model using OpenAI's API.

Important: You must have access to the GPT-4 API before this code will work.

# Prerequisites
- Access to the GPT-4 API
- Python 3.x installed
- Jupyter Notebook or Jupyter Lab installed
- Install the required libraries:
```
pip install ipywidgets requests
```

# Usage
- Clone the repository or copy the code provided above to a new Jupyter Notebook.
- Replace the api_key and org_number variables with your own GPT-4 API key and organization number.
```
api_key = "your_api-key"
org_number = "your_org_number"
```
- Run the code in the Jupyter Notebook. You will see a textarea to input your prompt, and buttons to submit the prompt or reset the conversation.
- Enter your prompt in the textarea and click "Submit" to send the prompt to the GPT-4 API. The response will be displayed below the buttons.
- To reset the conversation and start a new one, click "Reset".

# Code Overview
The code is organized in a single function main() that encapsulates the program's logic. It sets up the necessary widgets (input textarea, submit and reset buttons) and handles user interactions with the GPT-4 API.

The handle_submit() function is called when the user clicks the "Submit" button. It sends the user's input to the GPT-4 API and displays the response.

The handle_reset() function is called when the user clicks the "Reset" button. It clears the output and resets the conversation.

.cbrwx
