from IPython.display import display, Markdown
import requests
import json
import textwrap
import ipywidgets as widgets

def prompt_message(message, width=880):
    return textwrap.fill(message, width=width)

api_key = "your_api-key"
org_number = "your_org_number"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "OpenAI-Organization": org_number
}

def main():  # Main function to encapsulate the program's logic
    global messages, output, input_text

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    response_count = 0

    output = widgets.Output()

    def handle_reset(sender):
        nonlocal response_count
        response_count = 0
        output.clear_output()  # Remove the current main content
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},  # Reset the messages
        ]  # Call the main function again to "restart" the program
        input_text.value = ''

    def handle_submit(sender):
        nonlocal response_count
        user_input = input_text.value
        messages.append({"role": "user", "content": user_input})

        data = {
            "model": "gpt-4-0314", 
            "messages": messages,
            "max_tokens": 6000, # Adjust towards usage, or do a tokencount
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            response_json = response.json()
            content = response_json["choices"][0]["message"]["content"].strip()

            response_count += 1
            output.clear_output()  # Clear output
            with output:
                display(Markdown(f"<p style='color:limegreen;'>{'*' * 20} Response {response_count} {'*' * 20}</p>"))
                print(content)
            messages.append({"role": "assistant", "content": content})
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    input_text = widgets.Textarea(
        value='',
        placeholder='Enter your prompt here',
        description='Prompt:',
        disabled=False,
        rows=10,
        cols=80,
    )

    submit_button = widgets.Button(
        description="Submit",
        disabled=False,
    )

    reset_button = widgets.Button(
        description="Reset",
        disabled=False,
    )

    buttons = widgets.HBox([submit_button, reset_button])  # Create a horizontal box to display the buttons side by side

    display(input_text)
    display(buttons)
    display(output)

    submit_button.on_click(handle_submit)
    reset_button.on_click(handle_reset)

main()
