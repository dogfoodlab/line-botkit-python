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
    CameraAction,
    CameraRollAction,
    LocationAction,
    DatetimePickerAction,
    PostbackAction
)
from line_botkit import BotApp, BotHandler, BotContext


class HandleApp(BotApp):

    def start(self, handler: BotHandler):

        @handler.text(mode='*', text='handle app')
        def app(bot: LineBotApi, event: MessageEvent, context: BotContext):
            context.set_mode('')
            message1 = TextSendMessage(text='app: handle', quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1])

        @handler.text()
        def text(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: text (unhandled)')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.text(text='text1')
        def text1(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: text (text1)')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.text(text='text2')
        def text2(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: text (text2)')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.text(intent='intent1')
        def intent1(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: text (intent1)')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.text(intent='intent2')
        def intent2(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: text (intent2)')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.sticker()
        def sticker(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: sticker')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.image()
        def image(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: image')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.video()
        def video(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: video')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.audio()
        def audio(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: audio')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.location()
        def location(bot: LineBotApi, event: MessageEvent, context: BotContext):
            text = json.dumps(event.message.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: location')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

        @handler.postback()
        def postback(bot: LineBotApi, event: PostbackEvent, context: BotContext):
            text = json.dumps(event.postback.as_json_dict(), ensure_ascii=False)
            message1 = TextSendMessage(text='handle: postback')
            message2 = TextSendMessage(text=text, quick_reply=self.quick_reply())

            bot.reply_message(event.reply_token, [message1, message2])

    def quick_reply(self):
        return QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label='handle app', text='handle app')),
                QuickReplyButton(action=MessageAction(label='cache app', text='cache app')),
                QuickReplyButton(action=MessageAction(label='i18n app', text='i18n app')),
                QuickReplyButton(action=MessageAction(label='text1', text='text1')),
                QuickReplyButton(action=MessageAction(label='text2', text='text2')),
                QuickReplyButton(action=MessageAction(label='intent1 text', text='intent1 text')),
                QuickReplyButton(action=MessageAction(label='intent2 text', text='intent2 text')),
                QuickReplyButton(action=CameraAction(label='camera')),
                QuickReplyButton(action=CameraRollAction(label='camera roll')),
                QuickReplyButton(action=LocationAction(label='location')),
                QuickReplyButton(action=DatetimePickerAction(label='date picker', data='date picker', mode='date')),
                QuickReplyButton(action=PostbackAction(label='postback', data='postback'))
            ]
        )
