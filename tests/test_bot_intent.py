# -*- coding: utf-8 -*-
from line_botkit.bot_intent import BotIntent


def test_1():
    intent = BotIntent(intent_file='./tests/resources/intent.yml')

    assert intent.to_intent('test intent 1') == 'intent1'
    assert intent.to_intent('test intent 2') == 'intent2'

    assert intent.to_intent('dummy') is None
    assert intent.to_intent('') is None
    assert intent.to_intent(None) is None


def test_2():
    intent = BotIntent()

    assert intent.to_intent('test intent 1') is None
    assert intent.to_intent('test intent 2') is None

    assert intent.to_intent('dummy') is None
    assert intent.to_intent('') is None
    assert intent.to_intent(None) is None
