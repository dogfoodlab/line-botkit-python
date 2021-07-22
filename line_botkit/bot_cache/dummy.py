# -*- coding: utf-8 -*-
import logging
from typing import Dict, Any
from .base import BotCache

logger = logging.getLogger(__name__)


class DummyBotCache(BotCache):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.__cache: Dict[str, Dict[str, Any]] = {}

    def exists(self, key: str) -> bool:
        '''
        '''
        return (key in self.__cache.keys())

    def delete(self, key: str) -> bool:
        '''
        '''
        if key in self.__cache.keys():
            del(self.__cache[key])
            return True
        else:
            return False

    def set_obj(self, key: str, obj: Dict[str, Any]) -> None:
        '''
        '''
        self.__cache[key] = obj

    def get_obj(self, key: str) -> Dict[str, Any]:
        '''
        '''
        return self.__cache[key]

    def set_prop(self, key: str, prop: str, value: Any) -> None:
        '''
        '''
        self.__cache[key][prop] = value

    def get_prop(self, key: str, prop: str) -> Any:
        '''
        '''
        return self.__cache[key][prop]
