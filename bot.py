import telebot
from groq import Groq

client = Groq(api_key="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")
bot = telebot.TeleBot("7182390571:AAFPVDIzHtaenF6uZ9ln3t4zrctEiMEdq_c")
messages = []

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global messages
    messages.append({"role": "user", "content": message.text})
    if len(messages) > 6:
        messages = messages[-6:]
    response = client.chat.completions.create(model='llama3-70b-8192', messages=messages, temperature=0)
    bot.send_message(message.from_user.id, response.choices[0].message.content)
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

while True:
    bot.polling(none_stop=True, interval=0, timeout=0)
