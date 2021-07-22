# -*- coding: utf-8 -*-
from line_botkit.bot_locale import BotLocale


def test_1():
    locale = BotLocale()

    assert locale.locales_dir == './locales'
    assert locale.default == 'ja_JP'
    assert locale.fallback == 'en_US'


def test_2():
    locale = BotLocale(locales_dir='var1', default='var2', fallback='var3')

    assert locale.locales_dir == 'var1'
    assert locale.default == 'var2'
    assert locale.fallback == 'var3'
