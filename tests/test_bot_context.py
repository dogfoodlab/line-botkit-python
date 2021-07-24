# -*- coding: utf-8 -*-
from line_botkit.bot_context import BotContext
from line_botkit.bot_cache.dummy import DummyBotCache


def test_1(mocker):
    profile_mock = mocker.MagicMock()
    profile_mock.language = 'lang'
    bot_mock = mocker.MagicMock()
    bot_mock.get_profile.return_value = profile_mock

    context = BotContext(bot=bot_mock,
                         channel_id='channel',
                         user_id='user',
                         bot_cache=DummyBotCache())

    assert context.get_channel_id() == 'channel'
    assert context.get_user_id() == 'user'
    assert context.get_language() == 'lang'

    assert context.get_mode() == ''
    assert context.get_data() == {}
    assert context.get_tag() == ''

    assert context.set_mode('mode') is None
    assert context.set_data({'a': 'abc', 'b': 456}) is None
    assert context.set_tag('tag') is None

    assert context.get_mode() == 'mode'
    assert context.get_data() == {'a': 'abc', 'b': 456}
    assert context.get_tag() == 'tag'

    assert context.clear_data() is None

    assert context.get_mode() == 'mode'
    assert context.get_data() == {}
    assert context.get_tag() == 'tag'

    assert context.clear_tag() is None

    assert context.get_mode() == 'mode'
    assert context.get_data() == {}
    assert context.get_tag() == ''

    assert context.set_mode('mode') is None
    assert context.set_data({'a': 'abc', 'b': 456}) is None
    assert context.set_tag('tag') is None

    assert context.clear() is None

    assert context.get_mode() == 'mode'
    assert context.get_data() == {}
    assert context.get_tag() == ''
