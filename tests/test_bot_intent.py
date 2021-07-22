# -*- coding: utf-8 -*-
from line_botkit.bot_intent import BotIntent


def test_1(mocker):
    file_mock = mocker.MagicMock()
    file_mock.to_object.return_value = obj1

    intent = BotIntent(intent_file=file_mock)

    assert intent.to_intent('text1-1') == 'intent1'
    assert intent.to_intent('text1-2') == 'intent1'
    assert intent.to_intent('text2-1') == 'intent2'
    assert intent.to_intent('text2-2') == 'intent2'

    assert intent.to_intent('dummy') is None
    assert intent.to_intent('') is None
    assert intent.to_intent(None) is None


def test_2():
    intent = BotIntent(intent_file=None)

    assert intent.to_intent('text1-1') is None
    assert intent.to_intent('text1-2') is None
    assert intent.to_intent('text2-1') is None
    assert intent.to_intent('text2-2') is None

    assert intent.to_intent('dummy') is None
    assert intent.to_intent('') is None
    assert intent.to_intent(None) is None


obj1 = {
    'version': '1',
    'intents': {
        'intent1': {
            'texts': ['text1-1', 'text1-2']
        },
        'intent2': {
            'texts': ['text2-1', 'text2-2']
        }
    }
}
