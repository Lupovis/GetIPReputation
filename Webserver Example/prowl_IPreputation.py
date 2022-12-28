import requests
import os
import json
import subprocess

logfile = "/var/log/apache2/access.log"
#logfile = "access.log"

processed_ips = []

ips = []
with open(logfile) as f:
    for line in f:
        ips.append(line.split()[0])

ips = list(set(ips))

response_types = [
    "known-apache-attack"
    "known-bot",
    "known-brute-force-attack",
    "known-email-attack",
    "known-imap-attack",
    "known-ssh-attack",
    "known-voip-attack",
    "web-brute-force"
]

def process_ip(ip, flags):
    global processed_ips
    for flag in flags:
        if flag == "known-bot" or flag == "known-brute-force-attack" or flag == "web-brute-force" or flag not in response_types:
            # Block from accessing the entire network
            ip_tables_cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"
            os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing the network")
        elif flag == "known-apache-attack":
            # Change firewall settings to block this IP from accessing port 80 and 443
            ip_tables_cmds = [
                f"sudo iptables -A INPUT -p tcp --dport 80 -s {ip} -j DROP",
                f"sudo iptables -A INPUT -p tcp --dport 443 -s {ip} -j DROP"
            ]
            #ip_tables_cmd_to_unblock = f"sudo iptables -D INPUT -p tcp --dport 80 -s {ip} -j DROP"
            #os.system("sudo iptables -F")
            for ip_tables_cmd in ip_tables_cmds: 
                os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing port 80 and 443")
        elif flag == "known-email-attack":
            # Block from accessing email default ports (25, 465, 587)
            ip_tables_cmds = [
                f"sudo iptables -A INPUT -p tcp --dport 25 -s {ip} -j DROP",
                f"sudo iptables -A INPUT -p tcp --dport 465 -s {ip} -j DROP",
                f"sudo iptables -A INPUT -p tcp --dport 587 -s {ip} -j DROP"
            ] 
            for ip_tables_cmd in ip_tables_cmds:
                os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing email default ports (25, 465, 587)")
        elif flag == "known-imap-attack":
            # Block from accessing imap default ports (143, 993)
            ip_tables_cmds = [
                f"sudo iptables -A INPUT -p tcp --dport 143 -s {ip} -j DROP",
                f"sudo iptables -A INPUT -p tcp --dport 993 -s {ip} -j DROP"
            ]
            for ip_tables_cmd in ip_tables_cmds:
                os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing imap default ports (143, 993)")
        elif flag == "known-ssh-attack":
            # Block from accessing ssh default port (22)
            ip_tables_cmd = f"sudo iptables -A INPUT -p tcp --dport 22 -s {ip} -j DROP"
            os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing ssh default port (22)")
        elif flag == "known-voip-attack":
            # Block from accessing voip default ports (5060, 5061)
            ip_tables_cmds = [
                f"sudo iptables -A INPUT -p tcp --dport 5060 -s {ip} -j DROP",
                f"sudo iptables -A INPUT -p tcp --dport 5061 -s {ip} -j DROP"
            ]
            for ip_tables_cmd in ip_tables_cmds:
                os.system(ip_tables_cmd)
            print(f"Blocked {ip} from accessing voip default ports (5060, 5061)")

if __name__ == "__main__":
    with open("processed_ips.txt", "r") as f:
        processed_ips = f.read().splitlines()

    while True:
        ips = []
        with open(logfile) as f:
            for line in f:
                ips.append(line.split()[0])
        ips = list(set(ips))

        for ip in ips:
            #ip = '23.129.64.227'
            if ip not in processed_ips:
                response = requests.get(
                    "https://84h9dq7p3c.execute-api.eu-west-1.amazonaws.com/live/GetIPReputation",
                    params={"ip": ip},
                    headers={"x-api-key": "RcXcE6oFZb8Mn8bhNeDXT1qwaFZEOGKHag8ivBcB"},
                ).text
                #ip_ = '51.89.153.112'
                #response = "{'ip': '{ip_}', 'ttps': ['known-ssh-attack', 'known-apache-attack']}"
                flags = eval(response)["ttps"]
                process_ip(ip, flags)
                processed_ips.append(ip)
                with open("processed_ips.txt", "a") as f:
                    f.write(ip + "\n")