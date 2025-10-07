import requests
import os

url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
response = requests.get(url)
lines = response.text.splitlines()

loon_hosts = []
for line in lines:
    if line.startswith("0.0.0.0") or line.startswith("127.0.0.1"):
        parts = line.split()
        if len(parts) == 2:
            domain = parts[1]
            loon_hosts.append(f"{domain} = 0.0.0.0")

os.makedirs("StevenBlack-hosts", exist_ok=True)
with open("StevenBlack-hosts/loon-hosts.conf", "w") as f:
    f.write("[Host]\n")
    f.write("\n".join(loon_hosts))
