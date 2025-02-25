from server import Server, timing_decorator

class LinuxServer(Server):
    @timing_decorator
    def deploy_application(self):
        print(f"Deploying application on Linux server: {self.name}")
    
    @timing_decorator
    def stop_server(self):
        print(f"Stopping Linux server: {self.name}")
        self.server_status = "stopped"

    @staticmethod
    def get_server_info():
        return "Linux Server - Optimized for performance and security."