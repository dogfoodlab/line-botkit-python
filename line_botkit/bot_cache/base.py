# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class BotCache(metaclass=ABCMeta):
    '''
    '''

    @abstractmethod
    def exists(self, key: str) -> bool:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def delete(self, key: str) -> bool:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def set_obj(self, key: str, obj: Dict[str, Any]) -> None:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_obj(self, key: str) -> Dict[str, Any]:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def set_prop(self, key: str, prop: str, value: Any) -> None:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_prop(self, key: str, prop: str) -> Any:
        '''
        '''
        raise NotImplementedError()
