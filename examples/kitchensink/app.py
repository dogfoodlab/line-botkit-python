#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from flask import Flask, request
from line_botkit import (
    BotHandler,
    FlaskBotRequest,
    RedisBotCache,
    BotIntent,
    BotLocale
)
from apps import HandleApp, CacheApp, I18nApp

load_dotenv()

handler = BotHandler(
    bot_request=FlaskBotRequest(),
    bot_cache=RedisBotCache(),
    bot_locale=BotLocale(),
    bot_intent=BotIntent(intent_file='intent.yml'))

HandleApp().start(handler)
CacheApp().start(handler)
I18nApp().start(handler)

app = Flask(__name__)


@app.route('/bot01/channel01', methods=['POST'])
def webhook():
    return handler.handle(request)


if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)
