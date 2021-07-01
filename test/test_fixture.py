#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import pytest

@pytest.fixture
def connection(): # 1
    connection = sqlite3.connect(':memory:')
    yield connection
    connection.close()


@pytest.fixture(autouse=True)
def insert_one_item(connection): # 2
    session = connection.cursor()
    session.execute('''CREATE TABLE numbers
                          (id int , existing boolean)''')
    session.execute('INSERT INTO numbers VALUES (101, 1)')
    connection.commit()

def test_exist_num(connection): # 3
    session = connection.cursor()
    session.execute('''SELECT COUNT(1) FROM numbers WHERE id=101''')
    results = session.fetchall()
    assert len(results) > 0