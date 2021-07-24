# -*- coding: utf-8 -*-
from functools import wraps
from typing import Any
import json
import logging
import i18n
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError,
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    StickerMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    PostbackEvent
)
from .utils import line_util
from .bot_request.base import BotRequest
from .bot_cache.base import BotCache
from .bot_intent import BotIntent
from .bot_locale import BotLocale
from .bot_context import BotContext
from .bot_cache.dummy import DummyBotCache


logger = logging.getLogger()


class BotHandler:
    '''
    '''

    def __init__(self,
                 bot_request: BotRequest,
                 bot_cache: BotCache = None,
                 bot_intent: BotIntent = None,
                 bot_locale: BotLocale = None):
        '''
        '''
        # text func dict
        self.__intent_func_dic = {}
        self.__text_func_dic = {}
        self.__unhandled_func_dic = {}
        # media func dict
        self.__sticker_func_dic = {}
        self.__image_func_dic = {}
        self.__video_func_dic = {}
        self.__audio_func_dic = {}
        self.__location_func_dic = {}
        # postback func dict
        self.__postback_func_dic = {}

        # request
        self.__bot_request: BotRequest = bot_request

        # cache
        self.__bot_cache: BotCache = bot_cache or DummyBotCache()

        # intent
        self.__bot_intent: BotIntent = bot_intent or BotIntent()

        # i18n
        if bot_locale:
            i18n.set('filename_format', '{locale}.{format}')
            i18n.set('locale', bot_locale.default)
            i18n.set('fallback', bot_locale.fallback)
            i18n.load_path.append(bot_locale.locales_dir)

    #
    def trans(self, text: str, locale: str) -> str:
        '''
        '''
        return i18n.t(text, locale=locale)

    #
    def handle(self, request: Any) -> Any:
        '''
        '''
        body = self.__bot_request.get_body(request)

        if not len(json.loads(body)['events']):
            return self.__bot_request.create_response(200, '')

        signature = self.__bot_request.get_signature(request)

        channel_id = line_util.get_channel_id()
        channel_secret = line_util.get_channel_secret()
        channel_access_token = line_util.get_channel_access_token()

        line_bot_api = LineBotApi(channel_access_token)
        line_handler = WebhookHandler(channel_secret)

        user_id = json.loads(body)['events'][0]['source']['userId']

        context = BotContext(bot=line_bot_api,
                             channel_id=channel_id,
                             user_id=user_id,
                             bot_cache=self.__bot_cache)

        mode = context.get_mode()

        #
        @line_handler.add(MessageEvent, message=TextMessage)
        def handle_text_message(line_event: MessageEvent) -> None:
            '''
            '''
            text = str(line_event.message.text).strip()

            for tmp_mode in ['*', mode]:

                if tmp_mode in self.__intent_func_dic:
                    intent = self.__bot_intent.to_intent(text)
                    if intent in self.__intent_func_dic[tmp_mode]:
                        func = self.__intent_func_dic[tmp_mode][intent]
                        if func:
                            func(line_bot_api, line_event, context)
                            return

                if tmp_mode in self.__text_func_dic:
                    if text in self.__text_func_dic[tmp_mode]:
                        func = self.__text_func_dic[tmp_mode][text]
                        if func:
                            func(line_bot_api, line_event, context)
                            return

                if tmp_mode in self.__unhandled_func_dic:
                    func = self.__unhandled_func_dic[tmp_mode]
                    if func:
                        func(line_bot_api, line_event, context)
                        return

        #
        @line_handler.add(MessageEvent, message=StickerMessage)
        def handle_sticker_message(line_event: MessageEvent) -> None:
            '''
            '''
            if mode in self.__sticker_func_dic:
                func = self.__sticker_func_dic[mode]
                func(line_bot_api, line_event, context)

        #
        @line_handler.add(MessageEvent, message=ImageMessage)
        def handle_image_message(line_event: MessageEvent) -> None:
            '''
            '''
            if mode in self.__image_func_dic:
                func = self.__image_func_dic[mode]
                func(line_bot_api, line_event, context)

        #
        @line_handler.add(MessageEvent, message=VideoMessage)
        def handle_video_message(line_event: MessageEvent) -> None:
            '''
            '''
            if mode in self.__video_func_dic:
                func = self.__video_func_dic[mode]
                func(line_bot_api, line_event, context)

        #
        @line_handler.add(MessageEvent, message=AudioMessage)
        def handle_audio_message(line_event: MessageEvent) -> None:
            '''
            '''
            if mode in self.__audio_func_dic:
                func = self.__audio_func_dic[mode]
                func(line_bot_api, line_event, context)

        #
        @line_handler.add(MessageEvent, message=LocationMessage)
        def handle_location_message(line_event: MessageEvent) -> None:
            '''
            '''
            if mode in self.__location_func_dic:
                func = self.__location_func_dic[mode]
                func(line_bot_api, line_event, context)

        @line_handler.add(PostbackEvent)
        def handle_postback_event(line_event: PostbackEvent) -> None:
            '''
            '''
            if mode in self.__postback_func_dic:
                func = self.__postback_func_dic[mode]
                func(line_bot_api, line_event, context)

        #
        try:
            line_handler.handle(body, signature)

        except LineBotApiError as e:
            logger.error('LineBotApiError: {}'.format(e.message))
            return self.__bot_request.create_response(500, '')

        except InvalidSignatureError as e:
            logger.error('InvalidSignatureError: {}'.format(e.message))
            return self.__bot_request.create_response(400, '')

        return self.__bot_request.create_response(200, 'ok')

    #
    def text(self, mode: str = None, intent: str = None, text: str = None):
        def _text(func):
            set_mode = mode or ''

            # init
            if set_mode not in self.__intent_func_dic:
                self.__intent_func_dic[set_mode] = {}

            if set_mode not in self.__text_func_dic:
                self.__text_func_dic[set_mode] = {}

            if set_mode not in self.__unhandled_func_dic:
                self.__unhandled_func_dic[set_mode] = None

            # binding
            if intent:
                self.__intent_func_dic[set_mode][intent] = func

            elif text:
                self.__text_func_dic[set_mode][text] = func

            else:
                self.__unhandled_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _text

    #
    def sticker(self, mode: str = None):
        '''
        '''
        def _sticker(func):
            set_mode = mode or ''
            self.__sticker_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _sticker

    #
    def image(self, mode: str = None):
        '''
        '''
        def _image(func):
            set_mode = mode or ''
            self.__image_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _image

    #
    def video(self, mode: str = None):
        '''
        '''
        def _video(func):
            set_mode = mode or ''
            self.__video_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _video

    #
    def audio(self, mode: str = None):
        '''
        '''
        def _audio(func):
            set_mode = mode or ''
            self.__audio_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _audio

    #
    def location(self, mode: str = None):
        '''
        '''
        def _location(func):
            set_mode = mode or ''
            self.__location_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _location

    #
    def postback(self, mode: str = None):
        '''
        '''
        def _postback(func):
            set_mode = mode or ''
            self.__postback_func_dic[set_mode] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return _postback
