# -*- coding: utf-8 -*-
from line_botkit.bot_cache.redis import RedisBotCache


def test_0():
    assert isinstance(RedisBotCache(), RedisBotCache)


def test_1(mocker):
    redis_mock = mocker.MagicMock()
    redis_mock.exists.return_value = True

    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()
    setattr(cache, '_RedisBotCache__redis', redis_mock)

    assert cache.exists('key') is True


def test_2(mocker):
    redis_mock = mocker.MagicMock()
    redis_mock.delete.return_value = True

    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()
    setattr(cache, '_RedisBotCache__redis', redis_mock)

    assert cache.delete('key') is True


def test_3(mocker):
    redis_mock = mocker.MagicMock()
    redis_mock.hset.return_value = None

    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()
    setattr(cache, '_RedisBotCache__redis', redis_mock)

    assert cache.set_obj('key', {'a': 'abc', 'b': 123, 'c': {'c1': 'ccc', 'c2': 333}}) is None

    args, kwargs = redis_mock.hset.call_args

    assert args[0] == 'key'
    assert kwargs['mapping'] == {'a': '"abc"', 'b': '123', 'c': '{"c1": "ccc", "c2": 333}'}


def test_4(mocker):
    redis_mock = mocker.MagicMock()
    redis_mock.hgetall.return_value = {'a': '"abc"', 'b': '123', 'c': '{"c1": "ccc", "c2": 333}'}

    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()
    setattr(cache, '_RedisBotCache__redis', redis_mock)

    assert cache.get_obj('key') == {'a': 'abc', 'b': 123, 'c': {'c1': 'ccc', 'c2': 333}}

    args, kwargs = redis_mock.hgetall.call_args

    assert args[0] == 'key'


def test_5(mocker):
    redis_mock = mocker.MagicMock()
    redis_mock.hset.return_value = None

    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()
    setattr(cache, '_RedisBotCache__redis', redis_mock)

    assert cache.set_prop('key', 'a', 'abc') is None

    args, kwargs = redis_mock.hset.call_args

    assert args[0] == 'key'
    assert args[1] == 'a'
    assert args[2] == '"abc"'

    assert cache.set_prop('key', 'b', 123) is None

    args, kwargs = redis_mock.hset.call_args

    assert args[0] == 'key'
    assert args[1] == 'b'
    assert args[2] == '123'

    assert cache.set_prop('key', 'c', {'c1': 'ccc', 'c2': 333}) is None

    args, kwargs = redis_mock.hset.call_args

    assert args[0] == 'key'
    assert args[1] == 'c'
    assert args[2] == '{"c1": "ccc", "c2": 333}'


def test_6(mocker):
    mocker.patch.object(RedisBotCache, '__init__', return_value=None)
    cache = RedisBotCache()

    redis_mock = mocker.MagicMock()
    setattr(cache, '_RedisBotCache__redis', redis_mock)
    redis_mock.hget.return_value = '"abc"'

    assert cache.get_prop('key', 'a') == 'abc'

    args, kwargs = redis_mock.hget.call_args

    assert args[0] == 'key'
    assert args[1] == 'a'

    redis_mock.hget.return_value = '123'
    setattr(cache, '_RedisBotCache__redis', redis_mock)
    assert cache.get_prop('key', 'b') == 123

    args, kwargs = redis_mock.hget.call_args

    assert args[0] == 'key'
    assert args[1] == 'b'

    redis_mock.hget.return_value = '{"c1": "ccc", "c2": 333}'
    setattr(cache, '_RedisBotCache__redis', redis_mock)
    assert cache.get_prop('key', 'c') == {'c1': 'ccc', 'c2': 333}

    args, kwargs = redis_mock.hget.call_args

    assert args[0] == 'key'
    assert args[1] == 'c'
