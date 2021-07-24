# -*- coding: utf-8 -*-
import json
from linebot import LineBotApi
from linebot.models import (
    MessageEvent,
    PostbackEvent,
    TextSendMessage,
    QuickReply,
    QuickReplyButton,
    MessageAction,
    PostbackAction
)
from line_botkit import BotApp, BotHandler, BotContext


class CacheApp(BotApp):

    def start(self, handler: BotHandler):

        @handler.text(mode='*', text='cache app')
        def app(bot: LineBotApi, event: MessageEvent, context: BotContext):
            context.set_mode('cache')
            context.clear_tag()

            message1 = TextSendMessage(text='app: cache', quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1])

        @handler.text(mode='cache')
        def text(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = 'text unhandled'

            if context.get_tag() == 'prop1':
                data = context.get_data()
                data['prop1'] = event.message.text
                context.set_data(data)

                text = 'prop1 input: {}'.format(event.message.text)

            if context.get_tag() == 'prop2':
                data = context.get_data()
                data['prop2'] = event.message.text
                context.set_data(data)

                text = 'prop2 input: {}'.format(event.message.text)

            context.clear_tag()

            message1 = TextSendMessage(text=text, quick_reply=self.quick_reply())
            bot.reply_message(event.reply_token, [message1])

        @handler.postback(mode='cache')
        def postback(bot: LineBotApi, event: PostbackEvent, context: BotContext):
            context.clear_tag()

            if event.postback.data == 'dump':
                text = json.dumps(context.get_data(), ensure_ascii=False)
                message1 = TextSendMessage(text='cache: dump')
                message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

                bot.reply_message(event.reply_token, [message1, message2])
                return

            if event.postback.data == 'clear':
                context.clear_data()
                message1 = TextSendMessage(text='cache: clear', quick_reply=self.quick_reply())

                bot.reply_message(event.reply_token, [message1])
                return

            if event.postback.data == 'set_prop1':
                context.set_tag('prop1')
                message1 = TextSendMessage(text='input prop1')

                bot.reply_message(event.reply_token, [message1])
                return

            if event.postback.data == 'set_prop2':
                context.set_tag('prop2')
                message1 = TextSendMessage(text='input prop2')

                bot.reply_message(event.reply_token, [message1])
                return

    def quick_reply(self):
        return QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label='handle app', text='handle app')),
                QuickReplyButton(action=MessageAction(label='cache app', text='cache app')),
                QuickReplyButton(action=MessageAction(label='i18n app', text='i18n app')),
                QuickReplyButton(action=PostbackAction(label='set prop1', data='set_prop1')),
                QuickReplyButton(action=PostbackAction(label='set prop2', data='set_prop2')),
                QuickReplyButton(action=PostbackAction(label='dump', data='dump')),
                QuickReplyButton(action=PostbackAction(label='clear', data='clear'))
            ]
        )
