import os
import time
import requests


def warp_fresh():
    n = 10
    while n > 0:
        n = n - 1
        os.system("systemctl restart wg-quick@wg0")
        time.sleep(3)
        res = requests.get("https://www.cloudflare.com/cdn-cgi/trace")
        if res.status_code == 200 and "warp=on" in res.text:
            print("Succeed!")
            break
        else:
            continue
    else:
        requests.get("https://api.day.app/mXod6Bg3mnGbvXXR7edQoH/Failure!!!")


if __name__ == '__main__':
    time.sleep(30)
    warp_fresh()
    
