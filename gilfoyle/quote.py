import requests


def response(message):
    chatbot = requests.post(
        'http://localhost:5055/webhooks/rest/webhook',
        json={"sender": str(message.author), "message": str(message.content).lower()}
    )

    if len(chatbot.json()) > 0:
        return "```yaml\n" + chatbot.json()[0]['text'] + "\n```"
