# -*- coding: utf-8 -*-
from typing import Dict
import logging
from .core.file.base import CoreFile

logger = logging.getLogger(__name__)


class BotIntent:
    '''
    '''

    def __init__(self, intent_file: CoreFile):
        '''
        '''
        self.__intent_dic: Dict[str, str] = {}

        if intent_file:
            obj = intent_file.to_object()

            for intent in obj['intents']:
                for word in obj['intents'][intent]['texts']:
                    self.__intent_dic[word] = intent

    def to_intent(self, text: str) -> str or None:
        '''
        '''
        if text in self.__intent_dic:
            intent = self.__intent_dic[text]
            return intent
        else:
            return None
