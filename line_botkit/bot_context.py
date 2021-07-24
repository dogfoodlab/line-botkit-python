# -*- coding: utf-8 -*-
from typing import Dict, Any
import logging
from linebot import LineBotApi
from .bot_cache.base import BotCache

logger = logging.getLogger(__name__)

MODE: str = 'mode'
DATA: str = 'data'
TAG: str = 'tag'


class BotContext:
    '''
    '''

    def __init__(self, bot: LineBotApi, channel_id: str, user_id: str, bot_cache: BotCache):
        '''
        '''
        self.__bot: LineBotApi = bot
        self.__channel_id: str = channel_id
        self.__user_id: str = user_id
        self.__cache: BotCache = bot_cache

        self.__cache_key = '{}--{}'.format(channel_id, user_id)

        if not self.__cache.exists(self.__cache_key):
            self.__cache.set_obj(self.__cache_key,
                                 {MODE: '', DATA: {}, TAG: ''})

    #
    def get_channel_id(self) -> str:
        '''
        '''
        return self.__channel_id

    #
    def get_user_id(self) -> str:
        '''
        '''
        return self.__user_id

    #
    def get_language(self) -> str:
        '''
        '''
        return self.__bot.get_profile(self.__user_id).language

    #
    def set_mode(self, mode: str) -> None:
        '''
        '''
        self.__cache.set_prop(self.__cache_key, MODE, mode)

    #
    def get_mode(self) -> str:
        '''
        '''
        return self.__cache.get_prop(self.__cache_key, MODE)

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
        self.__cache.set_prop(self.__cache_key, DATA, {})

    #
    def set_data(self, data: Dict[str, Any]) -> None:
        '''
        '''
        self.__cache.set_prop(self.__cache_key, DATA, data)

    #
    def get_data(self) -> Dict[str, Any]:
        '''
        '''
        return self.__cache.get_prop(self.__cache_key, DATA)

    #
    def clear_tag(self) -> None:
        '''
        '''
        self.__cache.set_prop(self.__cache_key, TAG, '')

    #
    def set_tag(self, tag: str) -> None:
        '''
        '''
        self.__cache.set_prop(self.__cache_key, TAG, tag)

    #
    def get_tag(self) -> str:
        '''
        '''
        return self.__cache.get_prop(self.__cache_key, TAG)
