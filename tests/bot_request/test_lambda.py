# -*- coding: utf-8 -*-
from line_botkit.bot_request.awslambda import LambdaBotRequest


def test_1():
    input = {'headers': {'X-Line-Signature': 'sig1'}}
    request = LambdaBotRequest()

    assert request.get_signature(input) == 'sig1'


def test_2():
    input = {'headers': {'x-line-signature': 'sig2'}}
    request = LambdaBotRequest()

    assert request.get_signature(input) == 'sig2'


def test_3():
    input = {'headers': {}}
    request = LambdaBotRequest()

    assert request.get_signature(input) is None


def test_4():
    input = {'body': 'body1'}
    request = LambdaBotRequest()

    assert request.get_body(input) == 'body1'


def test_5():
    request = LambdaBotRequest()
    response = request.create_response(123, '456')

    assert response['isBase64Encoded'] is False
    assert response['statusCode'] == 123
    assert response['headers'] == {}
    assert response['body'] == '456'
