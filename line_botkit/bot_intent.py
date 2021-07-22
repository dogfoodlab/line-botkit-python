# -*- coding: utf-8 -*-
import yaml
from typing import Dict
import logging

logger = logging.getLogger(__name__)


class BotIntent:
    '''
    '''

    def __init__(self, intent_file: str = None):
        '''
        '''
        self.__intent_dic: Dict[str, str] = {}

        if intent_file:
            with open(intent_file) as fin:
                obj = yaml.safe_load(fin)

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
