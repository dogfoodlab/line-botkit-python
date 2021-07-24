# -*- coding: utf-8 -*-
from line_botkit.bot_i18n import BotI18n


def test_1(mocker):
    handler_mock = mocker.MagicMock()
    handler_mock.trans.return_value = 'test'

    i18n = BotI18n(handler=handler_mock, language='ja')

    assert i18n.trans('test') == 'test'

    args, kwargs = handler_mock.trans.call_args

    assert args[0] == 'test'
    assert args[1] == 'ja_JP'


def test_2(mocker):
    handler_mock = mocker.MagicMock()
    handler_mock.trans.return_value = 'test'

    i18n = BotI18n(handler=handler_mock, language='unknown')

    assert i18n.trans('test') == 'test'

    args, kwargs = handler_mock.trans.call_args

    assert args[0] == 'test'
    assert args[1] == 'unknown'
