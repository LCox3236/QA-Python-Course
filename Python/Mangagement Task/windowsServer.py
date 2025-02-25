from server import Server, timing_decorator

class WindowsServer(Server):
    @timing_decorator
    def deploy_application(self):
        print(f"Deploying application on Windows server: {self.name}")
    
    @timing_decorator
    def stop_server(self):
        print(f"Stopping Windows server: {self.name}")
        self.server_status = "stopped"
    
    @staticmethod
    def get_server_info():
        return "Windows Server - User-friendly with enterprise solutions."