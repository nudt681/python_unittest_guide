#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# content of test_with_mark.py
import pytest

@pytest.mark.finished
def test_func1():
    assert 1 == 1

@pytest.mark.unfinished
def test_func2():
    assert 1 != 1