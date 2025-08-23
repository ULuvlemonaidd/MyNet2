# MyNet2
mynet - Advanced Layer 4 & Layer 7 DDoS Simulation Tool

mynet is a command-line demonstration tool designed to simulate Distributed Denial-of-Service (DDoS) attacks at both the Transport Layer (Layer 4) and the Application Layer (Layer 7).

Originally created as a lightweight Layer 4 stress-testing utility, mynet has now expanded with a brand new, more powerful Layer 7 attack menu and upgraded Layer 4 methods (including cURL support). These additions make it a versatile tool for testing server resilience in a controlled, educational environment.

⚠️ Disclaimer
This tool is intended strictly for educational purposes and authorized testing only.
Do not use mynet on any network, server, or system you do not own or have explicit written permission to test.
Misuse can result in legal consequences. Always comply with applicable laws and terms of service.

🔧 Features
✅ New & More Powerful Layer 7 (Application Layer) Simulation

NEW HTTP Floods – simulate web-layer overloads

NEW cURL-based Floods – emulate realistic request-style traffic

NEW Hard Mode Attacks – optimized for maximum Layer 7 load testing

✅ Upgraded Layer 4 (Transport Layer) Simulation

TCP Flood – overwhelms target with TCP packets

UDP Flood – stronger, high-volume UDP traffic generation

SYN Flood – advanced half-open connection stressor

Heavy SYN / Hard UDP – upgraded high-load stressors

NEW cURL Floods at Layer 4 – hybrid simulation of connection + payload stress

✅ Multi-Bot Power

Increased bot capacity for distributed testing

Simulates coordinated attack power from multiple nodes

More realistic load-balancing & stress scenarios



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
