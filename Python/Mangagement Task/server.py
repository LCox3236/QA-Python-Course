from abc import ABC, abstractmethod
from typing import final
import time
class Server(ABC):
    def __init__(self, name):
        self._server_status = "stopped"
        self.name = name
        
    @abstractmethod
    def deploy_application(self):
        pass
    
    @abstractmethod
    def stop_server(self):
        pass
    
    @staticmethod
    def get_server_info():
        return "Generic Server - Used for hosting applications."
    
    @classmethod
    def get_server_type(cls):
        return cls.__name__
    
    @final
    def server_health_check(self):
        print(f"{self.name}: Server is healthy")
    
    @property
    def server_status(self):
        return self._server_status
    
    @server_status.setter
    def server_status(self, status):
        if status in ["running", "stopped"]:
            self._server_status = status
        else:
            raise ValueError("Status must be 'running' or 'stopped'")
        
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        pre_execution_time_stamp = time.time()
        result = func(*args, **kwargs)
        post_execution_time_stamp = time.time() - pre_execution_time_stamp
        print(f"{func.__name__} took {post_execution_time_stamp} seconds to execute")
        return result
    return wrapper