# -*- coding: utf-8 -*-
from typing import Dict
from .bot_handler import BotHandler

LOCALE_DIC: Dict[str, str] = {
    'ja': 'ja_JP'
}


class BotI18n:
    '''
    '''

    def __init__(self, handler: BotHandler, language: str):
        '''
        '''
        self.__handler: BotHandler = handler
        self.__locale: str = '__'

        if language in LOCALE_DIC:
            self.__locale = LOCALE_DIC[language]

    def trans(self, text: str) -> str:
        '''
        '''
        return self.__handler.trans(text, self.__locale)
