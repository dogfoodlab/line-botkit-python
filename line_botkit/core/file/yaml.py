# -*- coding: utf-8 -*-
from typing import Dict, Any
import yaml
from .base import CoreFile


class YamlFile(CoreFile):
    '''
    '''

    def __init__(self, file_path: str):
        '''
        '''
        self.__file_path = file_path

    def to_dict(self) -> Dict[str, Any]:
        '''
        '''
        with open(self.__file_path) as f:
            return yaml.safe_load(f)

    def to_bytes(self) -> Any:
        '''
        '''
        raise NotImplementedError()
