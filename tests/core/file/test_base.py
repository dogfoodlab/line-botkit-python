# -*- coding: utf-8 -*-
import pytest
from line_botkit.core.file.base import CoreFile


def test_0():
    with pytest.raises(TypeError):
        CoreFile()


def test_1():
    CoreFile.__abstractmethods__ = set()
    file = CoreFile()

    with pytest.raises(NotImplementedError):
        file.to_dict()

    with pytest.raises(NotImplementedError):
        file.to_bytes()
