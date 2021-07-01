# content in schedule.py
from src.demo.res import WorkerManager, ResourceManager


class Schedule:
    def __init__(self):
        self.work_mgr = WorkerManager()
        self.res_mgr = ResourceManager()

    def sch(self):
        ips = self.work_mgr.get_all_works()
        cpu_cost = [self.res_mgr.get_cpu_cost(ip) for ip in ips]
        min_cost_index = cpu_cost.index(min(cpu_cost)) # 获取负载最低的ip
        return ips[min_cost_index]