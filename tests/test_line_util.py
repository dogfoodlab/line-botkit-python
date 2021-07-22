# -*- coding: utf-8 -*-
import os
import pytest
from line_botkit import line_util


def test_1():
    os.environ['LINE_CHANNEL_ID'] = '123'
    result = line_util.get_channel_id()
    assert result == '123'


def test_2():
    os.environ.pop('LINE_CHANNEL_ID', None)
    with pytest.raises(ValueError):
        line_util.get_channel_id()


def test_3():
    os.environ['LINE_CHANNEL_SECRET'] = '456'
    result = line_util.get_channel_secret()
    assert result == '456'


def test_4():
    os.environ.pop('LINE_CHANNEL_SECRET', None)
    with pytest.raises(ValueError):
        line_util.get_channel_secret()


def test_5():
    os.environ['LINE_CHANNEL_ACCESS_TOKEN'] = '789'
    result = line_util.get_channel_access_token()
    assert result == '789'


def test_6():
    os.environ.pop('LINE_CHANNEL_ACCESS_TOKEN', None)
    with pytest.raises(ValueError):
        line_util.get_channel_access_token()
