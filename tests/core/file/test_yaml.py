# -*- coding: utf-8 -*-
import pytest
from line_botkit.core.file.yaml import YamlFile


def test_1():
    file = YamlFile(file_path='abc')
    assert file._YamlFile__file_path == 'abc'

    file = YamlFile(file_path='def')
    assert file._YamlFile__file_path == 'def'


def test_2(mocker):
    yaml = '''
    root:
        key1: abc
        key2: 123
        key3:
            prop1: def
            prop2: 456
    '''
    mock_io = mocker.mock_open(read_data=yaml)
    mocker.patch('builtins.open', mock_io)

    file = YamlFile(file_path='dummy')

    assert file.to_dict() == {'root': {'key1': 'abc', 'key2': 123, 'key3': {'prop1': 'def', 'prop2': 456}}}

    with pytest.raises(NotImplementedError):
        file.to_bytes()
