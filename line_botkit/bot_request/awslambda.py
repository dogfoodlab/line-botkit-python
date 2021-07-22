# -*- coding: utf-8 -*-
from typing import Dict, Any
import logging
from .base import BotRequest

logger = logging.getLogger(__name__)


class LambdaBotRequest(BotRequest):
    '''
    '''

    def get_signature(self, request: Dict[str, Any]) -> str:
        '''
        '''
        if 'X-Line-Signature' in request['headers']:
            signature = request['headers']['X-Line-Signature']

        elif 'x-line-signature' in request['headers']:
            signature = request['headers']['x-line-signature']

        return signature

    def get_body(self, request: Dict[str, Any]) -> str:
        '''
        '''
        return request['body']

    def create_response(self, status: int, message: str) -> Dict[str, Any]:
        '''
        '''
        return {
            'isBase64Encoded': False,
            'statusCode': status,
            'headers': {},
            'body': message
        }
