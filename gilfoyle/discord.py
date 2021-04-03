import requests


def on_message(message):
    chatbot = requests.post(
        'http://localhost:5005/webhooks/rest/webhook',
        json={"sender": message.author, "message": message.content}
    )

    if len(chatbot.json()) > 0:
        return chatbot.json()[0]['text']


if __name__ == '__main__':
    print(
        on_message(type('Message', (object,), {'content': 'je veux manger du chocolat', 'author': 'me'}))
    )
