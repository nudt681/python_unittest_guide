#
import ipaddress

from src.demo.schedule import ResourceManager, WorkerManager
from src.demo.schedule import Schedule
def mock_cpu_cost(ip):
    return int(ipaddress.IPv4Address(ip))


class TestSchedule:
    def test_sch(self,mocker):
        print(type(mocker))
        mocker.patch.object(ResourceManager, 'get_cpu_cost', side_effect=mock_cpu_cost)
        mocker.patch.object(WorkerManager, 'get_all_works', return_value=['1.1.1.1', '2.2.2.2'])
        sch = Schedule()
        res = sch.sch()
        assert res == '1.1.1.1'