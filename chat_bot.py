import google.generativeai as gpt

gpt.configure(api_key='AIzaSyBpx0ESiM3aYaqdQCKEXZL2OSIWy3K_c-Y')
geminipro = gpt.GenerativeModel('gemini-pro')

while True:
    if prompt.lower() == 'exit':
        break
    prompt = input("You: ")
    response = geminipro.generate_content(prompt)
    print(f"Bot: {response.text}")