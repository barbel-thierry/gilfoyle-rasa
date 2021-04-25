# Gilfoyle

![Tests](https://github.com/barbel-thierry/gilfoyle-rasa/workflows/Tests/badge.svg)
![Style](https://github.com/barbel-thierry/gilfoyle-rasa/workflows/Style/badge.svg)

#### powered by Rasa

* [Installation](https://github.com/barbel-thierry/gilfoyle-rasa#-installation)
    1. [Get the code](https://github.com/barbel-thierry/gilfoyle-rasa#-get-the-code)
    2. [Pre-process](https://github.com/barbel-thierry/gilfoyle-rasa#%EF%B8%8F-pre-process)
    3. [Start Gilfoyle](https://github.com/barbel-thierry/gilfoyle-rasa#-start-gilfoyle)
    4. [Create your bot application on Discord](https://github.com/barbel-thierry/gilfoyle-rasa#-create-your-bot-application-on-discord)
    5. [Train your model](https://github.com/barbel-thierry/gilfoyle-rasa#-train-your-model)
* [Check order](https://github.com/barbel-thierry/gilfoyle-rasa#-check-order)
* [Tips](https://github.com/barbel-thierry/gilfoyle-rasa#-tips)

## 💾 Installation

### 💻 Get the code

```shell
git clone git@github.com:barbel-thierry/gilfoyle-rasa.git
cd gilfoyle-rasa
cp .env.example .env # don't forget to fill in values

# setup Rasa & create a virtual environment
pip3 install rasa
pip3 install "rasa[spacy]"
python3 -m venv venv
source venv/bin/activate

# install requirements
pip install -U pip
pip install -r requirements.txt

# if you want to use any other language than english
python -m spacy download en_core_web_md
```

Rasa advises to pick the `md` version of any [language](https://spacy.io/usage/models#languages)

### ⚙️ Pre-process
* <dl>
  <dt>chatbot/domain.yml</dt>
  <dd>Where you define <i>intents</i> (ex: greeting, bye) and corresponding
    <i>responses</i> (ex: utter_greeting, utter_bye)</dd>
</dl>

* <dl>
  <dt>chatbot/data/nlu.yml</dt>
  <dd>Where you define what keywords could trigger each intent of yours</dd>
</dl>

* <dl>
  <dt>chatbot/data/stories.yml</dt>
  <dd>Where you describe the basic examples of your chatbot</dd>
</dl>

* <dl>
  <dt>chatbot/tests/test_stories.yml</dt>
  <dd>Where you set as many story examples as you want to make your
    chatbot more accurate</dd>
</dl>

* <dl>
  <dt>chatbot/data/rules.yml</dt>
  <dd>Where you set actions to perform when hapenning specific scenarios</dd>
</dl>

You can read more on [data format](https://rasa.com/docs/rasa/training-data-format/).

### 💪 Train your model

```shell
cd chatbot
rasa train
```

Other commands [here](https://rasa.com/docs/rasa/command-line-interface).

### 🦾 Create your bot application on Discord

Follow these [steps](https://discordpy.readthedocs.io/en/latest/discord.html).

### 💡 Start Gilfoyle

```shell
# from the root of gilfoyle-rasa
docker compose up --build -d
# or
docker compose up --build
```

Just wait for Rasa server to be started, and you're good to go!!!

## ✅ Check order

Gilfoyle will check for the first action filling requirements
(**in that very order**):

1.  Is it a scapegoat request?
    > Ex: <u>`@Gilfoyle`</u> who's the <u>goat</u>?<br>
    Gilfoyle will announce a random name from `SCAPEGOAT_TARGETS`
    

2.  Is it a request to get random values?
    > Ex: <u>`@Gilfoyle`</u> give me <u>luck</u><br> 
    Gilfoyle will announce random *number*, *letter*, *true*/*false*, *yes*/*no*,
    *heads*/*tails*, *direction*, *chifumi*
    

3.  Is it a game request?
    > Gilfoyle will announce a game launch / a victory (the `GAME_TRIGGER` has
    been posted, Gilfoyle will help you with the `GAME_RESPONSE` for you to be
    the first posting the `GAME_WINNING_ANSWER`)
    

4.  Is it a score request?
    > Ex: <u>`@Gilfoyle`</u> what's the <u>score</u>?<br>
    Gilfoyle will announce the current score board according to the
    `SCAPEGOAT_TARGETS` list provided and to the game results
    

5.  Is a word matching any NLU intent?
    > Gilfoyle will announce a quote linked with the previous posted message

## ✨ Tips

#### If you need an anonymous python object:

```python
type('anonymous_class_name', (object,), {'property_name':'property_value'})
```

#### If you want to test your chatbot locally:

```shell
docker exec -it gilfoyle /bin/bash
apt install curl
curl localhost:5055/webhooks/rest/webhook -d '{"sender": "me", "message": "Have you a Press pass?"}'
```

#### Slack (or others) can be used:

In this case, you would have to set up Flask (for instance) to expose
your `gilfoyle/main.py` and install SlackClient via pip
