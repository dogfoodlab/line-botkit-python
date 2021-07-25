# -*- coding: utf-8 -*-
from typing import Dict
import logging
from .core.file.yaml import YamlFile

logger = logging.getLogger(__name__)


class BotIntent:
    '''
    '''

    def __init__(self, intent_file: str = None):
        '''
        '''
        self.__intent_dic: Dict[str, str] = {}

        if intent_file:
            obj = YamlFile(file_path=intent_file).to_dict()

            for intent in obj['intents']:
                for word in obj['intents'][intent]['texts']:
                    self.__intent_dic[word] = intent

    def to_intent(self, text: str) -> str or None:
        '''
        '''
        return self.__intent_dic.get(text, None)
