import requests


def response(message):
    chatbot = requests.post(
        'http://localhost:5005/webhooks/rest/webhook',
        json={"sender": message.author, "message": message.content}
    )

    if len(chatbot.json()) > 0:
        return chatbot.json()[0]['text']
