#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# content of test_sample.py

def inc(x):
    return x + 1


def test_answer():
    print("111")
    assert inc(4) == 5
