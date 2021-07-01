# content in test_mock.py
import ipaddress
import unittest
from unittest import mock, TestCase

from src.demo.res import ResourceManager, WorkerManager
from src.demo.schedule import Schedule


def mock_cpu_cost(ip):
    return int(ipaddress.IPv4Address(ip))


class TestSchedule(TestCase):
    # mock对象的写法
    @mock.patch.object(ResourceManager, 'get_cpu_cost')
    @mock.patch.object(WorkerManager, 'get_all_works',return_value=['1.1.1.1', '2.2.2.2'])
    # mock方法的写法
    # @mock.patch('src.demo.res.ResourceManager.get_cpu_cost')
    # @mock.patch('src.demo.res.WorkerManager.get_all_works')
    def test_sch(self, _, cpu_cost):

        # workers = ['1.1.1.1', '2.2.2.2']
        cpu_cost.side_effect = mock_cpu_cost
        # all_workers.return_value = workers

        sch = Schedule()
        res = sch.sch()
        self.assertEqual(res, '1.1.1.1')


if __name__ == '__main__':
    unittest.main()
