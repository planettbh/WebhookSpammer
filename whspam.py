import requests
import json
import threading
import time

spam = input("Message to spam: ")
outputspam = spam + " | https://dsc.gg/hill"

url1 = ''
url2 = ''
url3 = ''
url4 = ''
url5 = ''
url6 = ''
url7 = ''
url8 = ''
url9 = ''
url10 = ''
url11 = ''
url12 = ''
url13 = ''
url14 = ''
url15 = ''


message = {
    'content': f'{outputspam}'
}

headers = {
    'Content-Type': 'application/json'
}

def wh1():
    response = requests.post(url1, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url2, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url3, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url4, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url5, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url6, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url7, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url8, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url9, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url10, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url11, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url12, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url13, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url14, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url15, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")

# Call send_message every 5 seconds using threading
def repeat_action(interval, action):
    while True:
        threading.Timer(interval, action).start()
        time.sleep(interval)

repeat_action(0, wh1)
