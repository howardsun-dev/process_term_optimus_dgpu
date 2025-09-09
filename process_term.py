import psutil

process_names = [
    "Adguard.exe",
    "Blip.exe",
    "Veeam.EndPoint.Tray.exe",
    "YourPhoneAppProxy.exe",
    "MicrosoftSecurityApp.exe",
]
found_names = set()

for proc in psutil.process_iter(["pid", "name"]):
    if proc.info["name"] in process_names:
        found_names.add(proc.info["name"])
        try:
            proc.kill()
            print(f"Process {proc.info['name']} (PID: {proc.info['pid']}) killed.")
        except psutil.NoSuchProcess:
            print(f"Process {proc.info['name']} (PID: {proc.info['pid']}) already terminated.")
        except psutil.AccessDenied:
            print(f"Access denied to terminate process {proc.info['name']} (PID: {proc.info['pid']}).")

for name in process_names:
    if name not in found_names:
        print(f"Process {name} is already terminated (not running).")
