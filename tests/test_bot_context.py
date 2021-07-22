# -*- coding: utf-8 -*-
from line_botkit.bot_context import BotContext
from line_botkit.bot_cache.dummy import DummyBotCache


def test_1():
    context = BotContext('key', DummyBotCache(), 'lang')

    assert context.get_laungage() == 'lang'

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
