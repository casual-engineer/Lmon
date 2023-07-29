import psutil
import socket
import sys
import time
import datetime

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_ipv4_address():
    try:
        # Get the default network interface's IPv4 address
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "N/A"

def get_system_uptime():
    boot_time_timestamp = psutil.boot_time()
    now_timestamp = time.time()
    uptime_seconds = now_timestamp - boot_time_timestamp
    return str(datetime.timedelta(seconds=uptime_seconds))

def get_hostname():
    return socket.gethostname()

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent if battery else "N/A"

def clear_console():
    if sys.platform.startswith('linux'):
        # Linux
        sys.stdout.write('\033[2J\033[H')
    elif sys.platform in ['win32', 'cygwin']:
        # Windows
        import os
        os.system('cls')
    elif sys.platform in ['darwin']:
        # macOS
        os.system('clear')

def get_top_cpu_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if process.info['cpu_percent'] > 0.0:
            processes.append(process.info)
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:3]

def get_top_memory_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'memory_percent']):
        if process.info['memory_percent'] > 0.0:
            processes.append(process.info)
    processes.sort(key=lambda x: x['memory_percent'], reverse=True)
    return processes[:3]

def main():
    print("Real-time System Usage Monitor (Press Ctrl+C to exit)")

    try:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            ipv4_address = get_ipv4_address()
            system_uptime = get_system_uptime()
            hostname = get_hostname()
            battery_percentage = get_battery_percentage()
            top_cpu_processes = get_top_cpu_processes()
            top_memory_processes = get_top_memory_processes()

            clear_console()

            print(f"Hostname: {hostname}")
            print(f"CPU Usage: {cpu_usage:.1f}%")
            print(f"Memory Usage: {memory_usage:.1f}%")
            print(f"Disk Usage: {disk_usage:.1f}%")
            print(f"IPv4 Address: {ipv4_address}")
            print(f"Battery Percentage: {battery_percentage}%")
            print(f"Uptime: {system_uptime}")

            print("\nTop 3 Processes by CPU Usage:")
            for process in top_cpu_processes:
                print(f"PID: {process['pid']} - Name: {process['name']} - CPU Usage: {process['cpu_percent']:.1f}%")

            print("\nTop 3 Processes by Memory Usage:")
            for process in top_memory_processes:
                print(f"PID: {process['pid']} - Name: {process['name']} - Memory Usage: {process['memory_percent']:.1f}%")

            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
