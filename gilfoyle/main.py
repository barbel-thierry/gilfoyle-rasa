from gilfoyle import quote, random_values


def on_message(message):
    if random_values.check(message):
        return random_values.global_result()
    else:
        return quote.response(message)


if __name__ == '__main__':
    print(
        on_message(type('Message', (object,), {'content': 'je veux manger du chocolat', 'author': 'me'}))
    )
