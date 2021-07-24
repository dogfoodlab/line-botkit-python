#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from flask import Flask, request
from linebot import LineBotApi
from linebot.models import MessageEvent, TextSendMessage
from line_botkit import (
    BotHandler,
    BotContext,
    FlaskBotRequest
)

load_dotenv()

handler = BotHandler(
    bot_request=FlaskBotRequest())


@handler.text()
def echo(bot: LineBotApi, event: MessageEvent, context: BotContext):
    bot.reply_message(event.reply_token,
                      TextSendMessage(text=event.message.text))


app = Flask(__name__)


@app.route('/bot01/channel01', methods=['POST'])
def webhook():
    return handler.handle(request)


if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)
