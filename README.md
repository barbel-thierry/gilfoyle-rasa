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

1.  Announce a random scapegoat according to the `SCAPEGOAT_TARGETS` list
    provided
    

2.  Announce random values (number, letter, true/false, yes/no,
    heads/tails, direction, chifoumi)
    

3.  Announce a game launch / a victory (the `GAME_TRIGGER` has been posted,
    Gilfoyle will help you with the `GAME_RESPONSE` for you to be the first
    posting the `GAME_WINNING_ANSWER`)
    

4.  Announce the current score board according to the `SCAPEGOAT_TARGETS` list
    provided and the game results
    

5.  Announce a film quote linked with the previous posted message

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
  <dt>gilfoyle/chatbot/domain.yml</dt>
  <dd>Where you define *intents* (ex: greeting, bye) and corresponding
    *responses* (ex: utter_greeting, utter_bye)</dd>
</dl>

* <dl>
  <dt>gilfoyle/chatbot/data/nlu.yml</dt>
  <dd>Where you define what words could trigger each intent of yours</dd>
</dl>

* <dl>
  <dt>gilfoyle/chatbot/data/stories.yml</dt>
  <dd>Where you describe the basic behavior of your chatbot</dd>
</dl>

* <dl>
  <dt>gilfoyle/chatbot/tests/test_stories.yml</dt>
  <dd>Where you set as many story examples as you want to make your
    chatbot more accurate</dd>
</dl>

* <dl>
  <dt>gilfoyle/chatbot/data/rules.yml</dt>
  <dd>Where you set the default action to perform when no other action
    is chosen</dd>
</dl>

### 💪 Train your model

```shell
cd gilfoyle/chatbot
rasa train
rasa interactive # if you want to train it from the CLI
```

### 💡 Start Gilfoyle

```shell
docker-compose up -d
# rasa run -m gilfoyle/chatbot/models --enable-api
```
