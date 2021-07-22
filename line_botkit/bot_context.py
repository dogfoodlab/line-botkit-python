# -*- coding: utf-8 -*-
from typing import Dict, Any
import logging
from .bot_cache.base import BotCache

logger = logging.getLogger(__name__)

MODE: str = 'mode'
DATA: str = 'data'
TAG: str = 'tag'


class BotContext:
    '''
    '''

    def __init__(self, cache_key: str, bot_cache: BotCache, language: str):
        '''
        '''
        self.__key: str = cache_key
        self.__cache: BotCache = bot_cache
        self.__language: str = language

        if not self.__cache.exists(self.__key):
            self.__cache.set_obj(self.__key,
                                 {MODE: '', DATA: {}, TAG: ''})

    #
    def get_laungage(self) -> str:
        '''
        '''
        return self.__language

    #
    def set_mode(self, mode: str) -> None:
        '''
        '''
        self.__cache.set_prop(self.__key, MODE, mode)

    #
    def get_mode(self) -> str:
        '''
        '''
        return self.__cache.get_prop(self.__key, MODE)

    #
    def clear(self) -> None:
        '''
        '''
        self.clear_data()
        self.clear_tag()

    #
    def clear_data(self) -> None:
        '''
        '''
        self.__cache.set_prop(self.__key, DATA, {})

    #
    def set_data(self, data: Dict[str, Any]) -> None:
        '''
        '''
        self.__cache.set_prop(self.__key, DATA, data)

    #
    def get_data(self) -> Dict[str, Any]:
        '''
        '''
        return self.__cache.get_prop(self.__key, DATA)

    #
    def clear_tag(self) -> None:
        '''
        '''
        self.__cache.set_prop(self.__key, TAG, '')

    #
    def set_tag(self, tag: str) -> None:
        '''
        '''
        self.__cache.set_prop(self.__key, TAG, tag)

    #
    def get_tag(self) -> str:
        '''
        '''
        return self.__cache.get_prop(self.__key, TAG)
