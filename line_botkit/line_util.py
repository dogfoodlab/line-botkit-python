# -*- coding: utf-8 -*-
import os
import logging

logger = logging.getLogger(__name__)


def get_channel_id() -> str:
    '''
    '''
    channel_id = os.getenv('LINE_CHANNEL_ID', None)

    if not channel_id:
        raise ValueError('NO LINE_CHANNEL_ID')

    return channel_id


def get_channel_secret() -> str:
    '''
    '''
    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

    if not channel_secret:
        raise ValueError('NO LINE_CHANNEL_SECRET')

    return channel_secret


def get_channel_access_token() -> str:
    '''
    '''
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

    if not channel_access_token:
        raise ValueError('NO LINE_CHANNEL_ACCESS_TOKEN')

    return channel_access_token
