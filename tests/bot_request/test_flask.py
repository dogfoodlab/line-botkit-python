# -*- coding: utf-8 -*-
from line_botkit.bot_request.flask import FlaskBotRequest


def test_1(mocker):
    flask_request_mock = mocker.MagicMock()
    flask_request_mock.headers = {'X-Line-Signature': 'sig1'}
    request = FlaskBotRequest()

    assert request.get_signature(flask_request_mock) == 'sig1'


def test_2(mocker):
    flask_request_mock = mocker.MagicMock()
    flask_request_mock.headers = {'x-line-signature': 'sig2'}
    request = FlaskBotRequest()

    assert request.get_signature(flask_request_mock) == 'sig2'


def test_3(mocker):
    flask_request_mock = mocker.MagicMock()
    flask_request_mock.headers = {}
    request = FlaskBotRequest()

    assert request.get_signature(flask_request_mock) is None


def test_4(mocker):
    flask_request_mock = mocker.MagicMock()
    flask_request_mock.get_data.return_value = 'body1'
    request = FlaskBotRequest()

    assert request.get_body(flask_request_mock) == 'body1'


def test_5():
    request = FlaskBotRequest()
    response = request.create_response(123, '456')

    assert response.status_code == 123
    assert response.response == [b'456']
    assert response.content_type == 'text/plain'
