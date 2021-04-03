from gilfoyle import quote


def on_message(message):
    return quote.response(message)


if __name__ == '__main__':
    print(
        on_message(type('Message', (object,), {'content': 'je veux manger du chocolat', 'author': 'me'}))
    )
