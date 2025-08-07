# MyNet2
mynet - Simple Layer 4 DDoS Simulation Tool
mynet is a lightweight, command-line demonstration tool designed to simulate Distributed Denial-of-Service (DDoS) attacks at the Transport Layer (Layer 4) using TCP, UDP, and SYN flood techniques. It also features an effective IP stressing and load-balancing network simulator, ideal for testing server resilience in a controlled environment.

⚠️ Disclaimer
This tool is intended strictly for educational purposes and authorized testing only. Do not use mynet on any network, server, or system that you do not own or have explicit written permission to test. Misuse can result in legal action and consequences. Always comply with all applicable laws and terms of service.

🔧 Features
✅ Supports multiple Layer 4 attack methods:

TCP flood

UDP flood

SYN flood

✅ Effective IP stress test 

✅ Load balancing simulation using  bot IPs

✅ Customizable attack settings:

Target IP and Port

Attack Method

Duration (10 to 9500 seconds)

Number of threads 


📦 Requirements
Python 3.x

Modules: socket, threading, random, time, sys, etc. (included in standard library)

Termux or ISH shell for deployment



---

Download commands (termux)

git clone https://github.com/ULuvlemonaidd/MyNet2

cd MyNet2

python mynet2.py

---

Download commands (ISH Shell)

apk add git

apk add python3

apk add py3-pip

git clone https://github.com/ULuvlemonaidd/MyNet2

cd MyNet2

python3 mynet2.py

<img width="616" height="415" alt="Screenshot 2025-07-18 3 16 44 AM" src="https://github.com/user-attachments/assets/0d1b6668-8886-4024-87a4-9df776d8c487" />
