# -*- coding: utf-8 -*-
from typing import Any
from abc import ABCMeta, abstractmethod


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
