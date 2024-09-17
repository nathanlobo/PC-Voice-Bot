# import google.generativeai as gpt

# gpt.configure(api_key='AIzaSyBpx0ESiM3aYaqdQCKEXZL2OSIWy3K_c-Y')
# geminipro = gpt.GenerativeModel('gemini-pro')

# while True:
#     if prompt.lower() == 'exit':
#         break
#     prompt = input("You: ")
#     response = geminipro.generate_content(prompt)
#     print(f"Bot: {response.text}")



import google.generativeai as gpt

gpt.configure(api_key='AIzaSyBpx0ESiM3aYaqdQCKEXZL2OSIWy3K_c-Y')
geminipro = gpt.GenerativeModel('gemini-pro')

chat_history = []

def update_chat_history(role, message):
    chat_history.append(f"{role}: {message}")

while True:
    prompt = input("You: ")
    
    update_chat_history("User", prompt)
    
    # Generate a response from the model
    response = geminipro.generate_content(prompt)
    bot_response = response.text
    
    # Update chat history with the bot's response
    update_chat_history("Bot", bot_response)
    
    print(f"Bot: {bot_response}")
