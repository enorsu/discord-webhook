import requests
import time
import random
import threading

start_screen = """
Discord webhook 'flooder'
Enter your url: """


url = input(start_screen)

amount = input("enter the amount of post requests to send: ")

data = {
    "content" : "",
    "username" : ""
}

headers = {
    "Content-Type": "application/json"
}



def post():
    return requests.post(url, json=data, headers=headers)

def randomword():
    return random.choice(open("words.txt").readlines())


def postmanytimes():
    for i in range(int(amount)):
        data["content"] = randomword()
        data["username"] = randomword()
        res = post()
        print(f"Request sent: {res.status_code}")
        if res.status_code.startswith("4") or res.status_code.startswith("5"):
            time.sleep(1.5)
        else:
            time.sleep(0.4)


thread_1 = threading.Thread(target=postmanytimes)
thread_1.start()



