# content in res.py
class ResourceManager:
    # 资源管理类
    def get_cpu_cost(self,ip):
        # 已经开发完的逻辑
        import requests
        import json
        response = requests.get("http://xx.oa.com/%s"%ip)
        rs = json.loads(response.json())
        return rs["num"]

class WorkerManager:
    def get_all_works(self):
        # 已经开发完的逻辑
        import pymysql
        # 打开数据库连接
        db = pymysql.connect("localhost", "xx", "xx", "TESTDB")
        cursor = db.cursor()
        cursor.execute("SELECT ip from works where alive=1")
        ips = cursor.fetchall()
        db.close()
        return [ip[0] for ip in ips]
