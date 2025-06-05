import requests
import os
import time

def clear():
    os.system("clear")

def banner():
    print("""
\033[1;31m
   .-"      "-.
  /            \\
 |              |
 |,  .-.  .-.  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
\033[1;36m
      Ghost IP Tool by Huseyn
\033[0m
""")

def my_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        print(f"\nYour public IP: \033[1;32m{ip}\033[0m\n")
    except:
        print("\033[1;31mCould not fetch IP\033[0m")

def ip_info(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        if r['status'] == 'success':
            print(f"""
IP: {r['query']}
Country: {r['country']}
City: {r['city']}
Region: {r['regionName']}
ISP: {r['isp']}
Timezone: {r['timezone']}
""")
        else:
            print("\033[1;31mInvalid IP or no data found.\033[0m")
    except:
        print("\033[1;31mError fetching IP info.\033[0m")

def main():
    while True:
        clear()
        banner()
        print("""
1) Show my public IP
2) Get info about an IP
3) Exit
""")
        choice = input("Choice: ")
        if choice == '1':
            my_ip()
            input("Press Enter...")
        elif choice == '2':
            ip = input("Enter IP: ")
            ip_info(ip)
            input("Press Enter...")
        elif choice == '3':
            break
        else:
            print("Invalid choice")
            time.sleep(1)

if __name__ == "__main__":
    main()
