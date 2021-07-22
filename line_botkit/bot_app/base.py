# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from line_botkit import BotHandler


class BotApp(metaclass=ABCMeta):
    '''
    '''

    @abstractmethod
    def start(self, handler: BotHandler) -> None:
        '''
        '''
        raise NotImplementedError()
