import asyncio
import websockets
import json
import psutil
import wmi
import socket

async def send_system_info():
    uri = "ws://127.0.0.1:8000/ws/system_info/"

    async with websockets.connect(uri) as websocket:
        while True:
            # Get the PC name
            pc_name = socket.gethostname()

            # Collect system information
            system_info = {
                "cpu_usage": psutil.cpu_percent(),
                "memory_usage": psutil.virtual_memory().percent,
                "ram_total": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # Total RAM in GB
                "ram_available": round(psutil.virtual_memory().available / (1024 ** 3), 2),  # Available RAM in GB
            }

            installed_apps = []
            w = wmi.WMI()
            for app in w.Win32_Product():
                installed_apps.append(app.Name)

            system_info["installed_apps"] = installed_apps

            data = {pc_name: {"system_info": system_info}}

            await websocket.send(json.dumps(data, indent=4))  

            await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_system_info())
