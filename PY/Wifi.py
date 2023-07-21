import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

wifi_name = run_command(["netsh", "wlan", "show", "interfaces"])
wifi_password = run_command(["netsh", "wlan", "show", "profile", "name=YOUR_WIFI_NAME", "key=clear"])

print("当前连接的WiFi名称：", wifi_name)
print("当前连接的WiFi密码：", wifi_password)