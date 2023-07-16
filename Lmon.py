import os
import psutil
import socket
import time


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_space():
    return psutil.disk_usage('/').percent

def get_ipv4_address():
    return socket.gethostbyname(socket.gethostname())

def get_router_ipv4_address():
    return socket.gethostbyname(socket.getfqdn())


while True:
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_space = get_disk_space()
    ipv4_address = get_ipv4_address()
    router_ipv4_address = get_router_ipv4_address()

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Space: {disk_space}%")
    print(f"IPv4 Address: {ipv4_address}")
    print(f"Router IPv4 Address: {router_ipv4_address}")
    print("-------------------------")

    time.sleep(1)
