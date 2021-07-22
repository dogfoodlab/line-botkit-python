# -*- coding: utf-8 -*-

class BotLocale:
    '''
    '''

    def __init__(self,
                 locales_dir: str = './locales',
                 default: str = 'ja_JP',
                 fallback: str = 'en_US'):
        '''
        '''
        self.locales_dir: str = locales_dir
        self.default: str = default
        self.fallback: str = fallback
