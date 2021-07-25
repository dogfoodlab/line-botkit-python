# -*- coding: utf-8 -*-
from typing import Dict, Any
from abc import ABCMeta, abstractmethod


class CoreFile(metaclass=ABCMeta):
    '''
    '''

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        '''
        '''
        raise NotImplementedError()

    @abstractmethod
    def to_bytes(self) -> Any:
        '''
        '''
        raise NotImplementedError()
