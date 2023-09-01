from time import sleep
import requests
def suggestion ():
    while True:
     url=requests.get("https://www.boredapi.com/api/activity")
     print(url.json()['activity'])
     sleep(2)


 