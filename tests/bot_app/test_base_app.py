# -*- coding: utf-8 -*-
import pytest
from line_botkit.bot_app.base import BotApp


def test_0():
    with pytest.raises(TypeError):
        BotApp()


def test_1():
    BotApp.__abstractmethods__ = set()
    app = BotApp()

    with pytest.raises(NotImplementedError):
        app.start(None)
