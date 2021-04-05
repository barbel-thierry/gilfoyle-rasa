#!/bin/sh

rasa run -m chatbot/models -p 5055 --enable-api & python3 gilfoyle/main.py
