from server import Server
from linuxServer import LinuxServer
from windowsServer import WindowsServer
# Demonstration
linux_server = LinuxServer("Linux-1")
windows_server = WindowsServer("Windows-1")

# Checking server types
print(linux_server.get_server_type())  # LinuxServer
print(windows_server.get_server_type())  # WindowsServer

# Deploying applications
linux_server.deploy_application()
windows_server.deploy_application()

# Checking and modifying server status
print(linux_server.server_status)  # stopped
linux_server.server_status = "running"
print(linux_server.server_status)  # running

# Server health check
linux_server.server_health_check()
windows_server.server_health_check()

# Modifying static method behavior
print(Server.get_server_info())  # Generic
print(LinuxServer.get_server_info())  # Linux specific
print(WindowsServer.get_server_info())  # Windows specific