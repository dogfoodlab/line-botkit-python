# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Any


class BotRequest(metaclass=ABCMeta):
    '''
    '''

    @abstractmethod
    def get_signature(self, request: Any) -> str:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_body(self, request: Any) -> str:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def create_response(self, status: int, message: str) -> Any:
        '''
        '''
        raise NotImplementedError()
