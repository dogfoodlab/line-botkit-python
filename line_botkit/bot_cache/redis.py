# -*- coding: utf-8 -*-
import os
from typing import Dict, Any
import json
import logging
import redis
from .base import BotCache

logger = logging.getLogger(__name__)


class RedisBotCache(BotCache):
    '''
    '''

    def __init__(self):
        '''
        '''
        connection_pool = redis.ConnectionPool(
            host=os.environ.get('REDIS_HOST', None),
            port=os.environ.get('REDIS_PORT', None),
            db=0,
            decode_responses=True)
        self.__redis = redis.StrictRedis(connection_pool=connection_pool)

    def exists(self, key: str) -> bool:
        '''
        '''
        return bool(self.__redis.exists(key))

    def delete(self, key: str) -> bool:
        '''
        '''
        return bool(self.__redis.delete(key))

    def set_obj(self, key: str, obj: Dict[str, Any]) -> None:
        '''
        '''
        mapping = {}
        for data_key in obj.keys():
            mapping[data_key] = json.dumps(obj[data_key], ensure_ascii=False)
        self.__redis.hset(key, mapping=mapping)

    def get_obj(self, key: str) -> Dict[str, Any]:
        '''
        '''
        data = {}
        mapping = self.__redis.hgetall(key)
        for data_key in mapping.keys():
            data[data_key] = json.loads(mapping[data_key])
        return data

    def set_prop(self, key: str, prop: str, value: Any) -> None:
        '''
        '''
        set_value = json.dumps(value, ensure_ascii=False)
        self.__redis.hset(key, prop, set_value)

    def get_prop(self, key: str, prop: str) -> Any:
        '''
        '''
        get_value = self.__redis.hget(key, prop)
        return json.loads(get_value)
