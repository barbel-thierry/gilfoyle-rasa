# Gilfoyle

![Tests](https://github.com/barbel-thierry/gilfoyle-rasa/workflows/Tests/badge.svg)
![Style](https://github.com/barbel-thierry/gilfoyle-rasa/workflows/Style/badge.svg)

#### powered by Rasa

## ❓What is this application for?

The purpose is to provide a Discord bot that will react (or not) when
specific words will be posted on your channel(s).

### ✅ Check order

Gilfoyle will check for the first action filling requirements
(**in that very order**):

1.  Is it a scapegoat request?
    > Ex: <u>`@Gilfoyle`</u> qui est <u>maudit</u> ?<br>
    Gilfoyle will announce a random name from `SCAPEGOAT_TARGETS`
    

2.  Is it a request to get random values?
    > Ex: <u>`@Gilfoyle`</u> donne moi des valeurs au <u>hasard</u><br> 
    Gilfoyle will announce random *number*, *letter*, *true*/*false*, *yes*/*no*,
    *heads*/*tails*, *direction*, *chifoumi*
    

3.  Is it a game request?
    > Gilfoyle will announce a game launch / a victory (the `GAME_TRIGGER` has
    been posted, Gilfoyle will help you with the `GAME_RESPONSE` for you to be
    the first posting the `GAME_WINNING_ANSWER`)
    

4.  Is it a score request?
    > Ex: <u>`@Gilfoyle`</u> quel est le <u>score</u> ?<br>
    Gilfoyle will announce the current score board according to the
    `SCAPEGOAT_TARGETS` list provided and the game results
    

5.  Is a word matching any NLU intent?
    > Gilfoyle will announce a quote linked with the previous posted message

## 💾 Installation

### 💻 Get the code

```shell
git clone git@github.com:barbel-thierry/gilfoyle-rasa.git
cd gilfoyle-rasa
cp .env.example .env # don't forget to fill in values

# update pip & create virtual environment
python3 -m pip install -U pip
python3 -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt
python -m spacy download fr-core-news-md # or whatever language you want
```

Rasa advises you to pick the `md` version of any [language](https://spacy.io/usage/models#languages)

### ⚙️ Pre-process
* <dl>
  <dt>chatbot/domain.yml</dt>
  <dd>Where you define <i>intents</i> (ex: greeting, bye) and corresponding
    <i>responses</i> (ex: utter_greeting, utter_bye)</dd>
</dl>

* <dl>
  <dt>chatbot/data/nlu.yml</dt>
  <dd>Where you define what words could trigger each intent of yours</dd>
</dl>

* <dl>
  <dt>chatbot/data/stories.yml</dt>
  <dd>Where you describe the basic behavior of your chatbot</dd>
</dl>

* <dl>
  <dt>chatbot/tests/test_stories.yml</dt>
  <dd>Where you set as many story examples as you want to make your
    chatbot more accurate</dd>
</dl>

* <dl>
  <dt>chatbot/data/rules.yml</dt>
  <dd>Where you set the default action to perform when no other action
    is chosen</dd>
</dl>

### 💪 Train your model

```shell
cd chatbot
rasa train
rasa shell # if you want to test it from the CLI
```

### 🦾 Create your bot application on Discord

Follow these [steps](https://discordpy.readthedocs.io/en/latest/discord.html)

### 💡 Start Gilfoyle

```shell
docker-compose up --build -d
# or
docker-compose up -d
```

If you want to test your chatbot locally:

```shell
docker exec -it gilfoyle /bin/bash
apt install curl
curl localhost:5055/webhooks/rest/webhook -d '{"sender": "me", "message": "dallas"}'
```

### ✨ Tips

```python
# anonymous object
type('anonymous_class_name', (object,), {'property_name':'property_value'})
```
