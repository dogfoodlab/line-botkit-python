# -*- coding: utf-8 -*-
import pytest
from line_botkit.bot_cache.base import BotCache


def test_0():
    with pytest.raises(TypeError):
        BotCache()


def test_1():
    BotCache.__abstractmethods__ = set()
    cache = BotCache()

    with pytest.raises(NotImplementedError):
        cache.exists('key')

    with pytest.raises(NotImplementedError):
        cache.delete('key')

    with pytest.raises(NotImplementedError):
        cache.set_obj('key', {})

    with pytest.raises(NotImplementedError):
        cache.get_obj('key')

    with pytest.raises(NotImplementedError):
        cache.set_prop('key', 'prop', {})

    with pytest.raises(NotImplementedError):
        cache.get_prop('key', 'prop')
