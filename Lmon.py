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

def main():
    print("Real-time System Usage Monitor (Press Ctrl+C to exit)")

    try:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            ipv4_address = get_ipv4_address()
            system_uptime = get_system_uptime()

            clear_console()

            print(f"CPU Usage: {cpu_usage:.1f}%")
            print(f"Memory Usage: {memory_usage:.1f}%")
            print(f"Disk Usage: {disk_usage:.1f}%")
            print(f"IPv4 Address: {ipv4_address}")
            print(f"Uptime: {system_uptime}")

            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
