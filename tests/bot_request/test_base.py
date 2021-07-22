# -*- coding: utf-8 -*-
import pytest
from line_botkit.bot_request.base import BotRequest


def test_0():
    with pytest.raises(TypeError):
        BotRequest()


def test_1():
    BotRequest.__abstractmethods__ = set()
    request = BotRequest()

    with pytest.raises(NotImplementedError):
        request.get_signature(request=None)

    with pytest.raises(NotImplementedError):
        request.get_body(request=None)

    with pytest.raises(NotImplementedError):
        request.create_response(status=123, message='456')
