# -*- coding: utf-8 -*-
import logging
from flask import Request, Response
from .base import BotRequest

logger = logging.getLogger(__name__)


class FlaskBotRequest(BotRequest):
    '''
    '''

    def get_signature(self, request: Request) -> str:
        '''
        '''
        if 'X-Line-Signature' in request.headers:
            signature = request.headers['X-Line-Signature']

        elif 'x-line-signature' in request.headers:
            signature = request.headers['x-line-signature']

        return signature

    def get_body(self, request: Request) -> str:
        '''
        '''
        return request.get_data(as_text=True)

    def create_response(self, status: int, message: str) -> Response:
        '''
        '''
        return Response(status=status, response=message, content_type='text/plain')
