# -*- coding: utf-8 -*-
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
from line_botkit import BotApp, BotHandler, BotContext, BotI18n


class I18nApp(BotApp):

    def start(self, handler: BotHandler):

        @handler.text(mode='*', text='i18n app')
        def app(bot: LineBotApi, event: MessageEvent, context: BotContext):
            context.set_mode('i18n')
            context.clear_tag()

            message1 = TextSendMessage(text='app: i18n', quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1])

        @handler.text(mode='i18n')
        def text(bot: LineBotApi, event: MessageEvent, context: BotContext):
            data = context.get_data()
            i18n = BotI18n(handler, data.get('lang', 'unknown'))
            message1 = TextSendMessage(text=i18n.trans(event.message.text), quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1])

        @handler.postback(mode='i18n')
        def postback(bot: LineBotApi, event: PostbackEvent, context: BotContext):

            if event.postback.data == 'set_ja':
                data = context.get_data()
                data['lang'] = 'ja'
                context.set_data(data)

                message1 = TextSendMessage(text='lang: ja', quick_reply=self.quick_reply())

                bot.reply_message(event.reply_token, [message1])
                return

            if event.postback.data == 'set_en':
                data = context.get_data()
                data['lang'] = 'en'
                context.set_data(data)

                message1 = TextSendMessage(text='lang: en', quick_reply=self.quick_reply())

                bot.reply_message(event.reply_token, [message1])
                return

            if event.postback.data == 'user_lang':
                text = 'user language: {}'.format(context.get_language())
                message1 = TextSendMessage(text=text, quick_reply=self.quick_reply())

                bot.reply_message(event.reply_token, [message1])
                return

    def quick_reply(self):
        return QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label='handle app', text='handle app')),
                QuickReplyButton(action=MessageAction(label='cache app', text='cache app')),
                QuickReplyButton(action=MessageAction(label='i18n app', text='i18n app')),
                QuickReplyButton(action=PostbackAction(label='set ja', data='set_ja')),
                QuickReplyButton(action=PostbackAction(label='set en', data='set_en')),
                QuickReplyButton(action=MessageAction(label='say hi', text='hi')),
                QuickReplyButton(action=MessageAction(label='say bye', text='bye')),
                QuickReplyButton(action=PostbackAction(label='user language', data='user_lang'))
            ]
        )
