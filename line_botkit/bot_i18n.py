# -*- coding: utf-8 -*-
from typing import Dict
from .bot_handler import BotHandler

LOCALE_DIC: Dict[str, str] = {
    'ja': 'ja_JP',
    'en': 'en_US'
}


class BotI18n:
    '''
    '''

    def __init__(self, handler: BotHandler, language: str):
        '''
        '''
        self.__handler: BotHandler = handler
        self.__locale: str = language

        if language in LOCALE_DIC:
            self.__locale = LOCALE_DIC[language]

    def trans(self, text: str, **kwargs) -> str:
        '''
        '''
        return self.__handler.trans(text, self.__locale, **kwargs)
