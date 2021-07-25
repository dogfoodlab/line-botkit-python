# -*- coding: utf-8 -*-
import os
from typing import Any
import json
from line_botkit.bot_handler import BotHandler
from line_botkit.bot_request.base import BotRequest
from line_botkit.bot_cache.dummy import DummyBotCache
from line_botkit.bot_intent import BotIntent
from line_botkit.bot_locale import BotLocale
from line_botkit.bot_context import BotContext
from linebot import (
    LineBotApi,
    WebhookHandler,
    SignatureValidator
)
from linebot.models import (
    MessageEvent
)
from linebot.exceptions import (
    LineBotApiError
)


def test_0_1():
    BotHandler(bot_request=None)


def test_0_2():
    BotHandler(bot_request=None,
               bot_cache=DummyBotCache())


def test_1_locale():
    handler = BotHandler(bot_request=None,
                         bot_locale=BotLocale(locales_dir='./tests/resources/locales'))

    assert handler.trans('test1', 'ja_JP') == 'テスト1'
    assert handler.trans('test1', 'en_US') == 'Test1'
    assert handler.trans('test1', '__') == 'Test1'

    assert handler.trans('test2', 'ja_JP') == 'Test2'
    assert handler.trans('test2', 'en_US') == 'Test2'
    assert handler.trans('test2', '__') == 'Test2'

    assert handler.trans('test3', 'ja_JP') == 'test3'
    assert handler.trans('test3', 'en_US') == 'test3'
    assert handler.trans('test3', '__') == 'test3'


def test_2_empty_request(mocker):
    create_line_bot_api_mock(mocker)

    handler = BotHandler(bot_request=TestBotRequest())

    assert handler.handle(body_empty) == {'status': 200, 'message': ''}


def test_3_api_error(mocker):
    create_line_bot_api_mock(mocker)

    error_mock = mocker.MagicMock()
    error_mock.message = 'test'

    error = LineBotApiError(500, {}, error=error_mock)
    mocker.patch.object(WebhookHandler, 'handle', side_effect=error)

    handler = BotHandler(bot_request=TestBotRequest())

    assert handler.handle(body_text1) == {'status': 500, 'message': ''}


def test_3_signature_error(mocker):
    create_line_bot_api_mock(mocker)

    mocker.patch.object(SignatureValidator, 'validate', return_value=False)

    handler = BotHandler(bot_request=TestBotRequest())

    assert handler.handle(body_text1) == {'status': 400, 'message': ''}


def test_3_exception(mocker):
    create_line_bot_api_mock(mocker)

    error_mock = mocker.MagicMock()
    error_mock.message = 'test'

    error = SystemError('error')
    mocker.patch.object(WebhookHandler, 'handle', side_effect=error)

    handler = BotHandler(bot_request=TestBotRequest())

    assert handler.handle(body_text1) == {'status': 500, 'message': ''}


def test_9_decorator(mocker):
    create_line_bot_api_mock(mocker)

    handler = BotHandler(
        bot_request=TestBotRequest(),
        bot_intent=BotIntent(intent_file='./tests/resources/intent.yml')
    )

    helper = Helper()

    #
    # mode=''
    #
    @handler.text()
    def text1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'text1'
        assert event.message.text == 'test text 1'
        assert context.get_mode() == ''
        helper.called.append('text1')

    @handler.text(text='test text 2')
    def text2(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'text2'
        assert event.message.text == 'test text 2'
        assert context.get_mode() == ''
        helper.called.append('text2')

    @handler.text(intent='intent1')
    def intent1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'intent1'
        assert event.message.text == 'test intent 1'
        assert context.get_mode() == ''
        helper.called.append('intent1')

    @handler.text(intent='intent2')
    def intent2(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'intent2'
        assert event.message.text == 'test intent 2'
        assert context.get_mode() == ''
        helper.called.append('intent2')

    @handler.sticker()
    def sticker1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'sticker'
        assert event.message.sticker_id == 'sticker1'
        assert event.message.package_id == 'package1'
        assert context.get_mode() == ''
        helper.called.append('sticker1')

    @handler.image()
    def image1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'image'
        assert event.message.id == 'image1'
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == ''
        helper.called.append('image1')

    @handler.video()
    def video1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'video'
        assert event.message.id == 'video1'
        assert event.message.duration == 9999
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == ''
        helper.called.append('video1')

    @handler.audio()
    def audio1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'audio'
        assert event.message.id == 'audio1'
        assert event.message.duration == 9999
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == ''
        helper.called.append('audio1')

    @handler.location()
    def location1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'location'
        assert event.message.id == 'location1'
        assert event.message.latitude == 35
        assert event.message.longitude == 135
        assert event.message.address == 'jp'
        assert context.get_mode() == ''
        helper.called.append('location1')

    @handler.postback()
    def postback1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'postback'
        assert event.postback.data == 'postback1'
        assert context.get_mode() == ''
        helper.called.append('postback1')

    #
    # mode='mode1'
    #
    @handler.text(mode='mode1')
    def text1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'text1'
        assert event.message.text == 'test text 1'
        assert context.get_mode() == 'mode1'
        helper.called.append('text1_mode1')

    @handler.text(mode='mode1', text='test text 2')
    def text2_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'text2'
        assert event.message.text == 'test text 2'
        assert context.get_mode() == 'mode1'
        helper.called.append('text2_mode1')

    @handler.text(mode='mode1', intent='intent1')
    def intent1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'intent1'
        assert event.message.text == 'test intent 1'
        assert context.get_mode() == 'mode1'
        helper.called.append('intent1_mode1')

    @handler.text(mode='mode1', intent='intent2')
    def intent2_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'text'
        assert event.message.id == 'intent2'
        assert event.message.text == 'test intent 2'
        assert context.get_mode() == 'mode1'
        helper.called.append('intent2_mode1')

    @handler.sticker(mode='mode1')
    def sticker1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'sticker'
        assert event.message.sticker_id == 'sticker1'
        assert event.message.package_id == 'package1'
        assert context.get_mode() == 'mode1'
        helper.called.append('sticker1_mode1')

    @handler.image(mode='mode1')
    def image1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'image'
        assert event.message.id == 'image1'
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == 'mode1'
        helper.called.append('image1_mode1')

    @handler.video(mode='mode1')
    def video1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'video'
        assert event.message.id == 'video1'
        assert event.message.duration == 9999
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == 'mode1'
        helper.called.append('video1_mode1')

    @handler.audio(mode='mode1')
    def audio1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'audio'
        assert event.message.id == 'audio1'
        assert event.message.duration == 9999
        assert event.message.content_provider.type == 'test'
        assert context.get_mode() == 'mode1'
        helper.called.append('audio1_mode1')

    @handler.location(mode='mode1')
    def location1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'message'
        assert event.message.type == 'location'
        assert event.message.id == 'location1'
        assert event.message.latitude == 35
        assert event.message.longitude == 135
        assert event.message.address == 'jp'
        assert context.get_mode() == 'mode1'
        helper.called.append('location1_mode1')

    @handler.postback(mode='mode1')
    def postback1_mode1(bot: LineBotApi, event: MessageEvent, context: BotContext):
        assert event.type == 'postback'
        assert event.postback.data == 'postback1'
        assert context.get_mode() == 'mode1'
        helper.called.append('postback1_mode1')

    #
    # request
    #

    #
    # mode=''
    #
    mocker.patch.object(BotContext, 'get_mode', return_value='')
    assert handler.handle(body_text1) == {'status': 200, 'message': ''}
    assert handler.handle(body_text2) == {'status': 200, 'message': ''}
    assert handler.handle(body_intent1) == {'status': 200, 'message': ''}
    assert handler.handle(body_intent2) == {'status': 200, 'message': ''}
    assert handler.handle(body_sticker1) == {'status': 200, 'message': ''}
    assert handler.handle(body_image1) == {'status': 200, 'message': ''}
    assert handler.handle(body_video1) == {'status': 200, 'message': ''}
    assert handler.handle(body_audio1) == {'status': 200, 'message': ''}
    assert handler.handle(body_location1) == {'status': 200, 'message': ''}
    assert handler.handle(body_postback1) == {'status': 200, 'message': ''}

    #
    # mode='mode1'
    #
    mocker.patch.object(BotContext, 'get_mode', return_value='mode1')
    assert handler.handle(body_text1) == {'status': 200, 'message': ''}
    assert handler.handle(body_text2) == {'status': 200, 'message': ''}
    assert handler.handle(body_intent1) == {'status': 200, 'message': ''}
    assert handler.handle(body_intent2) == {'status': 200, 'message': ''}
    assert handler.handle(body_sticker1) == {'status': 200, 'message': ''}
    assert handler.handle(body_image1) == {'status': 200, 'message': ''}
    assert handler.handle(body_video1) == {'status': 200, 'message': ''}
    assert handler.handle(body_audio1) == {'status': 200, 'message': ''}
    assert handler.handle(body_location1) == {'status': 200, 'message': ''}
    assert handler.handle(body_postback1) == {'status': 200, 'message': ''}

    assert helper.called == [
        #
        'text1',
        'text2',
        'intent1',
        'intent2',
        'sticker1',
        'image1',
        'video1',
        'audio1',
        'location1',
        'postback1',
        #
        'text1_mode1',
        'text2_mode1',
        'intent1_mode1',
        'intent2_mode1',
        'sticker1_mode1',
        'image1_mode1',
        'video1_mode1',
        'audio1_mode1',
        'location1_mode1',
        'postback1_mode1',
    ]


# helpers
class TestBotRequest(BotRequest):
    def get_signature(self, request: Any) -> str:
        return 'sig'

    def get_body(self, request: Any) -> str:
        return request

    def create_response(self, status: int, message: str) -> Any:
        return {'status': status, 'message': message}


def create_line_bot_api_mock(mocker):
    profile_mock = mocker.MagicMock()
    profile_mock.language.return_value = 'ja'
    mocker.patch.object(LineBotApi, 'get_profile', return_value=profile_mock)

    mocker.patch.object(SignatureValidator, 'validate', return_value=True)


class Helper():
    def __init__(self):
        self.called = []


os.environ['LINE_CHANNEL_ID'] = 'dummy_channel_id'
os.environ['LINE_CHANNEL_SECRET'] = 'dummy_channel_secret'
os.environ['LINE_CHANNEL_ACCESS_TOKEN'] = 'dummy_channel_token'

body_empty = json.dumps(
    {
        'events': []
    },
    ensure_ascii=False)

body_text1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'text',
                'id': 'text1',
                'text': 'test text 1'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }],
    },
    ensure_ascii=False)

body_text2 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'text',
                'id': 'text2',
                'text': 'test text 2'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }],
    },
    ensure_ascii=False)

body_intent1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'text',
                'id': 'intent1',
                'text': 'test intent 1'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }],
    },
    ensure_ascii=False)

body_intent2 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'text',
                'id': 'intent2',
                'text': 'test intent 2'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }],
    },
    ensure_ascii=False)

body_sticker1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'sticker',
                'stickerId': 'sticker1',
                'packageId': 'package1'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)

body_image1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'image',
                'id': 'image1',
                'contentProvider': {
                    'type': 'test'
                }
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)

body_video1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'video',
                'id': 'video1',
                'duration': 9999,
                'contentProvider': {
                    'type': 'test'
                }
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)

body_audio1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'audio',
                'id': 'audio1',
                'duration': 9999,
                'contentProvider': {
                    'type': 'test'
                }
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)

body_location1 = json.dumps(
    {
        'events': [{
            'type': 'message',
            'message': {
                'type': 'location',
                'id': 'location1',
                'latitude': 35,
                'longitude': 135,
                'address': 'jp'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)


body_postback1 = json.dumps(
    {
        'events': [{
            'type': 'postback',
            'postback': {
                'data': 'postback1'
            },
            'source': {
                'type': 'user',
                'userId': 'dummy_user_id'
            }
        }]
    },
    ensure_ascii=False)
