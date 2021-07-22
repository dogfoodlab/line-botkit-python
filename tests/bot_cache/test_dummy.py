# -*- coding: utf-8 -*-
from line_botkit.bot_cache.dummy import DummyBotCache


def test_0():
    assert isinstance(DummyBotCache(), DummyBotCache)


def test_1():
    cache = DummyBotCache()

    assert not cache.exists('key')

    assert cache.set_obj('key', {'a': 'abc', 'b': 123}) is None

    assert cache.exists('key')

    assert cache.get_obj('key') == {'a': 'abc', 'b': 123}

    assert cache.set_prop('key', 'a', 'def') is None

    assert cache.get_prop('key', 'a') == 'def'

    assert cache.set_prop('key', 'b', 456) is None

    assert cache.get_prop('key', 'b') == 456

    assert cache.set_prop('key', 'c', 'xxx') is None

    assert cache.get_prop('key', 'c') == 'xxx'

    assert cache.get_obj('key') == {'a': 'def', 'b': 456, 'c': 'xxx'}

    assert cache.delete('key') is True

    assert not cache.exists('key')

    assert not cache.delete('key')
