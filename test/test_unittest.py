#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # 单测启动前的准备工作，比如初始化一个mysql连接对象
        # 为了说明函数功能，测试的时候没有CMysql模块注释掉或者换做print学习
        # self.conn = CMysql()
        pass

    def tearDown(self):
        # 单测结束的收尾工作，比如数据库断开连接回收资源
        # self.conn.disconnect()
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()